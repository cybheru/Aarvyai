# Aarvyai V5 — Modular Windows Voice Assistant

Aarvyai is a Python voice assistant for Windows. Version 5 organizes voice input, command handling, Windows controls, and web shortcuts into separate modules.

## Features

- Speech input through SpeechRecognition and Google speech recognition (internet required).
- Spoken responses through pyttsx3.
- Greetings, current time and date.
- Google, YouTube, GitHub and Wikipedia searches.
- Opens common websites, including Gmail, GitHub, ChatGPT and Stack Overflow.
- Opens Calculator, Notepad, Paint, Chrome and Visual Studio Code when installed.
- Opens common user folders.
- Searches Desktop, Downloads and Documents for matching filenames (up to 10 results).
- Reports CPU, RAM and battery information when available.
- Stop, exit, quit and goodbye commands stop Aarvyai; they do not shut down Windows.

## Requirements

- Windows 10 or Windows 11.
- Python 3.9 or newer.
- Microphone and speakers.
- Internet access for speech recognition and web searches.

## Setup

Open PowerShell in the project directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PyAudio installation fails, use a supported Python version and Windows wheel for your architecture. Check Windows microphone privacy settings if the microphone cannot be opened.

## Run

```powershell
python main.py
```

Press Ctrl+C or say **stop** to exit.

## Example commands

| Say | Result |
|---|---|
| “Hello Aarvyai” | Greets you |
| “What time is it?” | Speaks the current time |
| “What is today's date?” | Speaks the date |
| “Search Google for Python” | Opens Google results |
| “Search YouTube for music” | Opens YouTube results |
| “Search GitHub for speech recognition” | Opens GitHub results |
| “Search Wikipedia for India” | Opens Wikipedia results |
| “Open Gmail” | Opens Gmail |
| “Open calculator” | Opens Calculator |
| “Open VS Code” | Opens Visual Studio Code |
| “Open Downloads” | Opens your Downloads folder |
| “Search file for budget” | Lists matching files in the terminal |
| “Show CPU”, “Show RAM”, “Show battery” | Reports system information |
| “Stop” | Exits Aarvyai |

## Project structure

```text
Aarvyai/
├── core/
│   └── assistant.py
├── pc/
│   └── pc_control.py
├── voice/
│   └── voice.py
├── web/
│   └── web_control.py
├── main.py
└── requirements.txt
```

## Notes

- Google speech recognition sends microphone audio to Google's recognition service.
- Searching files is limited to Desktop, Downloads and Documents. Matching file paths are printed in the terminal; files are not opened automatically.
- Microphone input and speech synthesis depend on local device and Windows configuration.
