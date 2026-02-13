import asyncio
import json
import websockets
import rtmidi
import sys

# MIDI Configuration
MIDI_PORT_NAME = "Leap Motion Bridge"

# CC Mappings
CC_PITCH = 10
CC_PAN   = 11
CC_MOD   = 1
CC_FILTER = 12

async def run_bridge():
    # 1. Setup MIDI
    midiout = rtmidi.MidiOut()
    ports = midiout.get_ports()
    print(f"Available MIDI ports: {ports}")
    
    # Prefer 'Midi Through' on Linux for reliability
    port_idx = next((i for i, p in enumerate(ports) if "Through" in p), 0)
    
    try:
        midiout.open_port(port_idx)
        print(f"Using MIDI Output: {ports[port_idx]}")
    except Exception as e:
        print(f"Error opening MIDI port: {e}")
        return

    # 2. Setup WebSocket
    uri = "ws://127.0.0.1:6437/v6.json"
    print(f"Connecting to Leap Bridge at {uri}...")
    
    async with websockets.connect(uri) as websocket:
        print("CONNECTED! Streaming Leap data to MIDI...")
        
        while True:
            try:
                msg = await websocket.recv()
                data = json.loads(msg)
                
                if "hands" in data and data["hands"]:
                    hand = data["hands"][0]
                    
                    # Y -> Pitch (CC 10)
                    y = hand["palmPosition"][1]
                    val_y = int(max(0, min(127, (y - 100) * 127 / 400)))
                    midiout.send_message([0xB0, CC_PITCH, val_y])
                    
                    # X -> Pan (CC 11)
                    x = hand["palmPosition"][0]
                    val_x = int(max(0, min(127, (x + 200) * 127 / 400)))
                    midiout.send_message([0xB0, CC_PAN, val_x])
                    
                    # Pinch -> Mod (CC 1)
                    pinch = hand["pinchStrength"]
                    val_pinch = int(pinch * 127)
                    midiout.send_message([0xB0, CC_MOD, val_pinch])
                    
                    print(f"Y: {val_y} | X: {val_x} | Pinch: {val_pinch}    ", end="\r")
                    
            except Exception as e:
                print(f"\nStream Error: {e}")
                break

if __name__ == "__main__":
    try:
        asyncio.run(run_bridge())
    except KeyboardInterrupt:
        print("\nStopping...")
