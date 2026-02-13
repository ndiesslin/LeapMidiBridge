# Gemini Project Context: Leap MIDI Bridge

## System Architecture
- **Hardware**: Leap Motion Controller.
- **Data Source**: Official WebSocket Bridge (`ws://localhost:6437/v6.json`).
- **Engine**: Python 3 + `mido` + `python-rtmidi`.
- **Output**: Virtual MIDI CC messages.

## MIDI Mapping (0-127)
- **CC 10**: Height (Palm Y).
- **CC 11**: Pan (Palm X).
- **CC 12**: Filter (Palm Z).
- **CC 1**: Modulation (Pinch).

## Portability
- **Linux**: Tested on Linux Mint. Uses ALSA/Jack.
- **Mac**: Compatible. Creates CoreMIDI Virtual Port.

## Commands
- **Run**: `./venv/bin/python bridge.py`
