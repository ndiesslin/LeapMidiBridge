import asyncio
import json
import websockets
import rtmidi

async def run():
    midiout = rtmidi.MidiOut()
    ports = midiout.get_ports()
    # Find any available port, preferably 'Through'
    port_idx = next((i for i, p in enumerate(ports) if "Through" in p), 0)
    midiout.open_port(port_idx)
    
    uri = "ws://127.0.0.1:6437/v6.json"
    print(f"Direct connection to {uri}")
    
    async with websockets.connect(uri) as ws:
        print("Connected!")
        while True:
            msg = await ws.recv()
            data = json.loads(msg)
            if "hands" in data and data["hands"]:
                h = data["hands"][0]
                y = int(max(0, min(127, (h["palmPosition"][1] - 100) * 127 / 400)))
                midiout.send_message([0xB0, 10, y])
                print(f"Sent MIDI: {y}", end="\r")

if __name__ == "__main__":
    asyncio.run(run())
