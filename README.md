# Aarvyai V4 — Guru AI PC Voice Assistant

Aarvyai V4 is a beginner-friendly Windows voice assistant. It listens for spoken commands, speaks responses, opens supported applications and common folders, searches common user folders for files, and reports CPU, RAM, and battery information.

## Features

- Voice input with SpeechRecognition and Google speech recognition (internet required).
- Spoken output with pyttsx3.
- Greetings, current time, and date.
- Google and YouTube web searches.
- Opens Google, YouTube, Gmail, GitHub, and ChatGPT.
- Opens Calculator, Notepad, Paint, WordPad, Chrome, and Visual Studio Code when installed.
- Opens Desktop, Downloads, Documents, Pictures, Music, and Videos folders.
- Searches Desktop, Downloads, and Documents for matching file names. If there is one exact match, Aarvyai asks before opening it.
- Reports CPU and RAM use and battery status when the device exposes that information.
- Stop, exit, quit, and goodbye commands stop Aarvyai; they do not shut down Windows.

## Requirements

- Windows 10 or Windows 11.
- Python 3.9 or newer.
- A working microphone and speakers.
- Internet access for voice recognition and web searches.

## Setup (Windows)

1. Install Python 3.9 or newer and enable **Add Python to PATH** in the installer.
2. Open PowerShell in this project folder.
3. (Recommended) Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the requirements:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

   If PyAudio installation fails, use a Python version and wheel supported by your Windows architecture, then retry `python -m pip install PyAudio`. Microphone access must be enabled in Windows privacy settings.

## Run

```powershell
python main.py
```

Press `Ctrl+C` or say **stop** to exit.

## Example voice commands

| Say | What Aarvyai does |
|---|---|
| “Hello Guru” | Greets you |
| “What time is it?” | Speaks the current time |
| “What is today's date?” | Speaks the date |
| “Search Google for Python” | Opens Google search results |
| “Search YouTube for music” | Opens YouTube search results |
| “Open Gmail” | Opens Gmail |
| “Open calculator” | Opens Calculator |
| “Open VS Code” | Opens Visual Studio Code |
| “Open Downloads” | Opens your Downloads folder |
| “Search file for budget” | Searches Desktop, Downloads, and Documents |
| “Show CPU” / “Show RAM” / “Show battery” | Reports system information |
| “Show system information” | Reports CPU, RAM, and battery information |
| “Stop” | Exits Aarvyai |

## Troubleshooting

- **Microphone error:** Check that Windows allows desktop apps to use the microphone and that the correct input device is connected.
- **Speech recognition unavailable:** Check the internet connection; Google recognition is an online service.
- **No speech heard:** Check the Windows output device and pyttsx3 voice settings.
- **Application not found:** Install the app. Chrome and VS Code are detected from common Windows install locations or PATH.
- **Battery unavailable:** Desktop PCs and some devices do not provide battery sensor data; this is expected.
- **No matching file:** Search is limited to Desktop, Downloads, and Documents to avoid scanning the whole computer.

## Project files

```text
Aarvyai/
├── .gitignore
├── CHANGELOG.md
├── README.md
├── VERSION
├── main.py
└── requirements.txt
```

## Version

Current version: **4.0.0**. See [VERSION](VERSION) and [CHANGELOG.md](CHANGELOG.md).
