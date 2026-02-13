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

## How to use with a DAW (FL Studio, Ableton, Logic, etc.)
The bridge creates a virtual MIDI controller that your music software sees as a physical hardware device.

### On the machine running the bridge:
1. **Start the bridge**: Run `python bridge.py`.
2. **Open your DAW**: Launch FL Studio, Ableton Live, Logic Pro, etc.
3. **Enable the Input**:
   - Go to **MIDI Settings / Preferences**.
   - Look for **"Leap Motion Bridge"** (Mac) or **"Midi Through"** (Linux).
   - Click **Enable**.
4. **Map a Parameter (MIDI Learn)**:
   - **FL Studio**: Right-click any knob (e.g., Cutoff) -> Select **"Link to controller..."** -> Move your hand.
   - **Ableton**: Press `Ctrl+M` -> Click a knob -> Move your hand -> Press `Ctrl+M` again.
   - **Logic**: Press `Cmd+L` -> Move a screen knob -> Move your hand.

### Control Mappings
- **Move Hand Up/Down**: Controls mapped parameters via **CC 10**.
- **Move Hand Left/Right**: Controls mapped parameters via **CC 11**.
- **Pinch Fingers**: Controls mapped parameters via **CC 1** (Mod Wheel).

## Use Case: Cross-Machine Control
If your Leap Motion is plugged into a Linux machine but your DAW is on a different Windows/Mac computer:
1. Use a Network MIDI tool like **rtpMIDI** (Windows) or built-in **Network MIDI** (macOS).
2. Route the "Midi Through" port on Linux to the Network MIDI session.
3. Your DAW will receive the hand movements over your local network!
