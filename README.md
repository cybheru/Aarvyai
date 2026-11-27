# Aarvyai V6 — Hindi + English Voice Assistant

Aarvyai is a beginner-friendly Python voice assistant for Windows. V6 keeps the English commands from V5 and adds common Hindi and Hinglish commands written in Roman letters.

## Features

- Speech input through SpeechRecognition and Google speech recognition (internet required).
- Spoken responses through pyttsx3.
- English and common Hinglish voice commands, such as “YouTube kholo”, “Time kya hua hai”, and “Calculator open karo”.
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
| “Hello Aarvyai” or “Namaste” | Greets you |
| “What time is it?” or “Time kya hua hai?” | Speaks the current time |
| “What is today's date?” or “Aaj ki date batao” | Speaks the date |
| “Search Google for Python” or “Google par Python search karo” | Opens Google results |
| “Search YouTube for music” or “YouTube par music search karo” | Opens YouTube results |
| “Search GitHub for speech recognition” | Opens GitHub results |
| “Search Wikipedia for India” | Opens Wikipedia results |
| “Open Gmail” | Opens Gmail |
| “Open calculator” or “Calculator open karo” | Opens Calculator |
| “Open VS Code” | Opens Visual Studio Code |
| “Open Downloads” or “Downloads kholo” | Opens your Downloads folder |
| “Search file for budget” | Lists matching files in the terminal |
| “Show CPU”, “RAM dikhao”, “Show battery” | Reports system information |
| “Stop” | Exits Aarvyai |

Hindi/Hinglish support covers common Romanized phrases. The speech recognition service may recognize Hindi and Hinglish differently depending on pronunciation and internet connection; repeat or rephrase a command if needed.

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
├── requirements.txt
├── VERSION
├── CHANGELOG.md
└── README.md
```

## Notes

- Google speech recognition sends microphone audio to Google's recognition service.
- Searching files is limited to Desktop, Downloads and Documents. Matching file paths are printed in the terminal; files are not opened automatically.
- Microphone input and speech synthesis depend on local device and Windows configuration.
- Aarvyai is made by Bheru.
