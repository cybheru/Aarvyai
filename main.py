
import importlib
try:
    pyttsx3 = importlib.import_module("pyttsx3")
except ModuleNotFoundError as error:
    if error.name != "pyttsx3":
        raise
    raise RuntimeError(
        "pyttsx3 is not installed. Install it with: "
        "python -m pip install pyttsx3"
    ) from error
import webbrowser
import subprocess
import shutil
from datetime import datetime
from urllib.parse import quote_plus
from pathlib import Path

try:
    sr = importlib.import_module("speech_recognition")
except ModuleNotFoundError as error:
    if error.name != "speech_recognition":
        raise
    raise RuntimeError(
        "SpeechRecognition is not installed. Install it with: "
        "python -m pip install SpeechRecognition"
    ) from error


# ==========================================
# GURU AI - V3 SMART COMMANDS
# ==========================================

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()


def speak(text):
    """Speak a message and display it."""
    print(f"\nAarvya AI: {text}")

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as error:
        print(f"Speech output error: {error}")


def listen():
    """Listen to the microphone and recognize speech."""

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source, duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        print("Recognizing...")
        command = recognizer.recognize_google(audio)

        print(f"You: {command}")
        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected.")

    except sr.UnknownValueError:
        print("Speech was not understood.")

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")

    except OSError:
        speak("Microphone error. Check your microphone.")

    except Exception as error:
        print(f"Listening error: {error}")

    return ""


# ==========================================
# APPLICATION LAUNCHER
# ==========================================

def open_application(app_name):
    """Launch supported applications on Windows."""

    commands = {
        "calculator": ["calc.exe"],
        "notepad": ["notepad.exe"],
    }

    if app_name == "chrome":
        # Check common Chrome installation locations.
        possible_paths = [
            Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
            Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
            Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe",
        ]

        for path in possible_paths:
            if path.is_file():
                try:
                    subprocess.Popen([str(path)])
                    speak("Opening Chrome.")
                    return
                except OSError:
                    continue

        # Try Chrome if it is available through PATH.
        chrome = shutil.which("chrome")
        if chrome:
            try:
                subprocess.Popen([chrome])
                speak("Opening Chrome.")
                return
            except OSError:
                pass

        speak(
            "Chrome was not found. "
            "Please check its installation."
        )
        return

    if app_name == "vs code":
        code = shutil.which("code")

        if code:
            try:
                subprocess.Popen([code])
                speak("Opening Visual Studio Code.")
            except OSError:
                speak("Could not open Visual Studio Code.")
        else:
            speak(
                "VS Code was not found in PATH. "
                "You can open it manually or configure its path."
            )
        return

    try:
        subprocess.Popen(commands[app_name])
        speak(f"Opening {app_name}.")
    except (OSError, KeyError):
        speak(f"Could not open {app_name}.")


# ==========================================
# WEB SEARCH AND WEBSITE FUNCTIONS
# ==========================================

def google_search(query):
    """Search Google for the given query."""
    if not query.strip():
        speak("Please tell me what you want to search.")
        return

    url = "https://www.google.com/search?q=" + quote_plus(query)
    webbrowser.open(url)
    speak(f"Searching Google for {query}.")


def youtube_search(query):
    """Search YouTube for the given query."""
    if not query.strip():
        speak("Please tell me what you want to search.")
        return

    url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )
    webbrowser.open(url)
    speak(f"Searching YouTube for {query}.")


def open_website(command):
    """Open a supported website or a valid web address."""

    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
    }

    target = command.strip().lower()

    # Match a known website name.
    for name, url in websites.items():
        if target == name:
            webbrowser.open(url)
            speak(f"Opening {name}.")
            return True

    # Allow explicit HTTP/HTTPS addresses only.
    if target.startswith(("https://", "http://")):
        webbrowser.open(target)
        speak("Opening website.")
        return True

    return False


# ==========================================
# COMMAND HANDLER
# ==========================================

def handle_command(command):

    if not command:
        return True

    # Exit commands
    if command in ("exit", "quit", "stop", "goodbye", "shutdown guru"):
        speak("Goodbye! Guru AI is shutting down.")
        return False

    # Greetings
    if any(word in command for word in (
        "hello", "hi guru", "hey guru",
        "good morning", "good afternoon", "good evening"
    )):
        speak("Hello! I am Guru AI. How can I help you?")
        return True

    # Time
    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return True

    # Date
    if "date" in command or "today" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}.")
        return True

    # Google search
    if command.startswith("search google for "):
        google_search(command.removeprefix("search google for "))
        return True

    if command.startswith("google search "):
        google_search(command.removeprefix("google search "))
        return True

    # YouTube search
    if command.startswith("search youtube for "):
        youtube_search(command.removeprefix("search youtube for "))
        return True

    if command.startswith("youtube search "):
        youtube_search(command.removeprefix("youtube search "))
        return True

    # Applications
    app_commands = {
        "calculator": ("calculator", ("open calculator", "start calculator")),
        "notepad": ("notepad", ("open notepad", "start notepad")),
        "chrome": ("chrome", ("open chrome", "start chrome")),
        "vs code": ("vs code", (
            "open vs code", "open vscode",
            "open visual studio code", "start vs code"
        )),
    }

    for app_name, (app_key, phrases) in app_commands.items():
        if command in phrases:
            open_application(app_key)
            return True

    # Website shortcuts
    if command.startswith("open "):
        target = command.removeprefix("open ").strip()

        if open_website(target):
            return True

        # If the target is an unknown site, don't guess or execute it.
        speak(
            "I don't recognize that website. "
            "Try Google, YouTube, Gmail, GitHub, or ChatGPT."
        )
        return True

    # Unknown command
    speak(
        "Sorry, I don't understand that command yet. "
        "Please try another command."
    )
    return True


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    print("=" * 45)
    print("          Aarvya AI - V2")
    print("          SMART COMMANDS")
    print("=" * 45)

    speak("Hello! Aarvya ru AI version 3 is ready.")

    while True:
        command = listen()

        if not handle_command(command):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAarvya AI stopped by keyboard.")
    finally:
        try:
            engine.stop()
        except Exception:
            pass
