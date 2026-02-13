# Leap Motion MIDI Bridge (Hyperion Edition)

A professional-grade spatial MIDI controller utility for **Ultraleap Hyperion**. Converts hand tracking data into MIDI CC messages.

## MIDI Mapping
| Control | MIDI CC | Description |
| :--- | :--- | :--- |
| **Palm Y** | **CC 10** | Vertical height (Pitch/Frequency) |
| **Palm X** | **CC 11** | Horizontal position (Pan) |
| **Pinch** | **CC 1** | Modulation Wheel (Trigger/Effects) |

## Setup & Running

### 1. Build and Start the Bridge
Ensure your Leap Motion is plugged in and the tracking bridge is running:
```bash
cd ~/projects/AirTouchCanvas/UltraleapTrackingWebSocket/build
./Ultraleap-Tracking-WS &
```

### 2. Start the MIDI Bridge
```bash
cd ~/projects/LeapMidiBridge
./venv/bin/python bridge.py
```

## How to use for Making Music (Linux)
The bridge sends data to the system **"Midi Through"** port.

1. **Open a Synth**: Launch a program like **amsynth** or **ZynAddSubFX**.
2. **Route MIDI**: Use `aconnect` or a visual tool like **QjackCtl** to connect "Midi Through" to your Synth.
   - *Example*: `aconnect 14:0 <synth_port_id>`
3. **Midi Learn**: Right-click any knob in your synth (like "Filter Cutoff") and choose "Midi Learn". Move your hand up and down—the knob will now follow your hand!

## How to use for Making Music (Mac)
1. Run the script as usual. It will create a virtual port called **"Leap Motion Bridge"**.
2. Open **Ableton, Logic, or GarageBand**.
3. The port will appear in your MIDI Preferences automatically.
