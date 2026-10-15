# Aarvyai

Aarvyai is a Python voice-assistant prototype for hands-free everyday tasks.

## Features

- Recognizes voice commands with SpeechRecognition and responds with pyttsx3 text-to-speech.
- Gives the current time and date and responds to greetings.
- Searches Google and YouTube from spoken queries.
- Opens Google, YouTube, Gmail, GitHub, and ChatGPT.
- Launches Calculator, Notepad, Chrome, and Visual Studio Code on Windows.
- Exits on commands such as “stop”, “exit”, “quit”, or “goodbye”.

## Requirements

- Python 3.9 or newer
- A working microphone and speakers
- An internet connection for Google speech recognition
- Windows for the built-in desktop application shortcuts

## Setup

Install the dependencies listed in requirements.txt:

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Example voice commands

- “What time is it?”
- “What is today's date?”
- “Search Google for Python”
- “Search YouTube for music”
- “Open Gmail”
- “Open calculator”
- “Open VS Code”
- “Stop”

The project is an early-stage prototype. Microphone and speech-engine setup can vary by system.
