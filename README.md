# Leap Motion MIDI Bridge

A cross-platform (Mac/Linux) Python utility that converts Leap Motion hand tracking data into MIDI Control Change (CC) messages.

## Features
- **Palm Y (Height)** -> **MIDI CC 10**
- **Palm X (Horizontal)** -> **MIDI CC 11**
- **Palm Z (Depth)** -> **MIDI CC 12**
- **Pinch Strength** -> **MIDI CC 1 (Modulation)**

## Requirements
1. **Ultraleap Hyperion** (Service + WebSocket Bridge running).
2. **Python 3.8+**.
3. **MIDI Sink**: A DAW (Bitwig, Ableton, Logic) or a standalone synth (amsynth).

## Setup & Running

### 1. Install Dependencies
```bash
python3 -m venv venv
./venv/bin/pip install mido python-rtmidi websockets
```

### 2. Run the Bridge
```bash
./venv/bin/python bridge.py
```

## Mac vs Linux
- **Mac**: Automatically creates a virtual MIDI port named "Leap Motion Bridge" that appears in Logic/Ableton.
- **Linux**: On most distros, this will create an ALSA MIDI port. You may need to use a tool like `aconnect` or `QjackCtl` to route it to your software if it doesn't auto-detect.
