# Aarvyai -v0.1

Aarvyai is a simple Python voice-assistant prototype that explores speech recognition and spoken responses.

## Features

- Listens for spoken commands with SpeechRecognition.
- Replies using text-to-speech with pyttsx3.
- Handles greetings and requests for the current time or date.
- Includes shortcuts intended to open Google, YouTube, and WhatsApp.
- Recognizes stop, exit, and quit as exit commands.

## Requirements

- Python 3
- A working microphone and speakers
- An internet connection for Google speech recognition

## Setup

Install the Python packages used by the project:

```bash
python -m pip install SpeechRecognition pyttsx3 click PyAudio
```

## Run

```bash
python main.py
```

## Example commands

- "What time is it?"
- "What is today's date?"
- "Open Google"
- "Open YouTube"
- "Open WhatsApp"
- "Stop"

This is an early-stage project; microphone and speech-engine setup can vary by system.
