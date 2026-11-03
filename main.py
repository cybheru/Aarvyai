
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
import os

try:
    psutil = importlib.import_module("psutil")
except ModuleNotFoundError as error:
    if error.name != "psutil":
        raise
    psutil = None

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
# Aarvya  AI - V4 PC ASSISTTANT
#windows version 
# ==========================================

# engine = pyttsx3.init()
# engine.setProperty("rate", 170)
# engine.setProperty("volume", 1.0)

# recognizer = sr.Recognizer()
# recognizer.pause_threshold = 0.8

# #-------------- VOICE OUTPUT------------

# def speak(text):
#     """Speak a message and display it."""
#     print(f"\nAarvya AI: {text}")

#     try:
#         engine.say(text)
#         engine.runAndWait()
#     except Exception as error:
#         print("Speech output error: error")
# #--------------- VOICE INPUT---------------

# def listen():
   
#     try:
#         with sr.Microphone() as source:
#             print("\nListening...")

#             recognizer.adjust_for_ambient_noise(
#                 source, duration=0.5
#             )

#             audio = recognizer.listen(
#                 source,
#                 timeout=5,
#                 phrase_time_limit=10
#             )

#         print("Recognizing...")
#         command = recognizer.recognize_google(audio)

#         print(f"You: command")
#         return command.lower().strip()

#     except sr.WaitTimeoutError:
#         print("No speech detected.")

#     except sr.UnknownValueError:
#         print("Speech was not understood.")

#     except sr.RequestError:
#         speak("Speech recognition service is unavailable.")

#     except OSError:
#         speak("Microphone error. Check your microphone.")

#     except Exception as error:
#         print(f"Listening error: error")

#     return ""


# # ==========================================
# #--------APPLICATIONs---------
# # ==========================================

# def open_application(app_name):
    
#     commands = {
#         "calculator": ["calc.exe"],
#         "notepad": ["notepad.exe"],
#         "paint": ["mspaint.exe"],
#         "wordpad":["write.exe"],

#     }

#     if app_name == "chrome":
#         # Check common Chrome installation locations.
#         possible_paths = [
#             Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
#             Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
#             Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe",
#         ]

#         for path in possible_paths:
#             if path.is_file():
#                 try:
#                     subprocess.Popen([str(path)])
#                     speak("Opening Chrome.")
#                     return
#                 except OSError:
#                     pass

#         # Try Chrome if it is available through PATH.
#         chrome = shutil.which("chrome")
#         if chrome:
#             try:
#                 subprocess.Popen([chrome])
#                 speak("Opening Chrome.")
#                 return
#             except OSError:
#                 pass

#         speak(
#             "Chrome was not found on this computer. "
#             "Please check its installation."
#         )
#         return

#     if app_name == "vs code":
#         code_path = shutil.which("code")

#         if not code_path:
#             possible_paths = [
#                 path.home() / "AppData/Local/Programs/Microsoft VS Code/Code.exe",
#                 path("C:/Program Files/Microsoft VS Code/Code.exe"),
#             ]

#             for path in possible_paths:
#                 if path.is_file():
#                     code_path = str(path)
#                     break

#         if code_path:
#             try:
#                 subprocess.Popen([code_path])
#                 speak("Opening Visual Studio Code.")
#             except OSError:
#                 speak("Could not open Visual Studio Code.")
#         else:
#             speak(
#                 "VS Code was not found in PATH. "
                
#             )
#         return

#     try:
#         subprocess.Popen(app_commands[app_name])
#         speak(f"Opening {app_name}.")
#     except (OSError, KeyError):
#         speak(f"Could not open {app_name}.")


# #-------------FOLDERS-----------------------

# def get_folder():
#     home = Path.home()

#     return {
#         "desktop": home / "Desktop",
#         "downloads": home / "Downloads",
#         "documents": home / "Documents",
#         "pictures": home / "Pictures",
#         "music": home / "Music",
#         "videos": home / "Videos",
        
#     }

# def open_folder(folder_name):
#     folders = get_folders()
#     folder = folders.get(folder_name)

#     if folder and folder.is_dir():
#         try:
#             os.startfile(file(folder))
#             speak(f"Opening{folder_name}.")

#         except OSError:
#             speak("I could not open that folder.")

#         else:
#             speak(f"The {folder_name} folder was not found.")


# #-------------FILE SEARCH-------------

# def search_file(filename):
#     filename = filename.strip().strip("\"'")

#     if not filename:
#         speak("Please trll me the file name.")
#         return

#     # Search only common user folders.
#     #This avoids scanning the entire computer.

#     search_folders = [
#         path.home() / "Desktop",
#         path.home() / "Downloads",
#         path.home() / "Documents",
              
#     ]

#     result = []
#     maximum_result = 10

#     speak(f"Searching for {filename}.")

#     for folder in search_folders:
#         if not folder.is_dir():
#             continue

#         try:
#             for Path in folder.rglob("*"):
#                 if path.is_file() and filename.casefold() in Path.name.casefold():
#                     results.append(Path)

#                     if len(results) >= maximum_result:
#                         break
#         except(OSError,PermissionError):
#             continue
#         if len(results) >= maximum_results:
#             break
#     if not results:
#         speak("No matching files were found in Desktop, Downloads, or Documents.")   
#         return

#     print("\nMatching files:")

#     for index, path in enumerate(results,start=1):
#         print(f"I found {len(results)}matching file or files.")

#         #



# # ==========================================
# # WEB SEARCH AND WEBSITE FUNCTIONS
# # ==========================================

# def google_search(query):
#     """Search Google for the given query."""
#     if not query.strip():
#         speak("Please tell me what you want to search.")
#         return

#     url = "https://www.google.com/search?q=" + quote_plus(query)
#     webbrowser.open(url)
#     speak(f"Searching Google for {query}.")


# def youtube_search(query):
#     """Search YouTube for the given query."""
#     if not query.strip():
#         speak("Please tell me what you want to search.")
#         return

#     url = (
#         "https://www.youtube.com/results?search_query="
#         + quote_plus(query)
#     )
#     webbrowser.open(url)
#     speak(f"Searching YouTube for {query}.")


# def open_website(command):
#     """Open a supported website or a valid web address."""

#     websites = {
#         "google": "https://www.google.com",
#         "youtube": "https://www.youtube.com",
#         "gmail": "https://mail.google.com",
#         "github": "https://github.com",
#         "chatgpt": "https://chatgpt.com",
#     }

#     target = command.strip().lower()

#     # Match a known website name.
#     for name, url in websites.items():
#         if target == name:
#             webbrowser.open(url)
#             speak(f"Opening {name}.")
#             return True

#     # Allow explicit HTTP/HTTPS addresses only.
#     if target.startswith(("https://", "http://")):
#         webbrowser.open(target)
#         speak("Opening website.")
#         return True

#     return False


# # ==========================================
# # COMMAND HANDLER
# # ==========================================

# def handle_command(command):

#     if not command:
#         return True

#     # Exit commands
#     if command in ("exit", "quit", "stop", "goodbye", "shutdown guru"):
#         speak("Goodbye! Guru AI is shutting down.")
#         return False

#     # Greetings
#     if any(word in command for word in (
#         "hello", "hi guru", "hey guru",
#         "good morning", "good afternoon", "good evening"
#     )):
#         speak("Hello! I am Guru AI. How can I help you?")
#         return True

#     # Time
#     if "time" in command:
#         current_time = datetime.now().strftime("%I:%M %p")
#         speak(f"The current time is {current_time}.")
#         return True

#     # Date
#     if "date" in command or "today" in command:
#         current_date = datetime.now().strftime("%d %B %Y")
#         speak(f"Today's date is {current_date}.")
#         return True

#     # Google search
#     if command.startswith("search google for "):
#         google_search(command.removeprefix("search google for "))
#         return True

#     if command.startswith("google search "):
#         google_search(command.removeprefix("google search "))
#         return True

#     # YouTube search
#     if command.startswith("search youtube for "):
#         youtube_search(command.removeprefix("search youtube for "))
#         return True

#     if command.startswith("youtube search "):
#         youtube_search(command.removeprefix("youtube search "))
#         return True

#     # Applications
#     app_commands = {
#         "calculator": ("calculator", ("open calculator", "start calculator")),
#         "notepad": ("notepad", ("open notepad", "start notepad")),
#         "chrome": ("chrome", ("open chrome", "start chrome")),
#         "vs code": ("vs code", (
#             "open vs code", "open vscode",
#             "open visual studio code", "start vs code"
#         )),
#     }

#     for app_name, (app_key, phrases) in app_commands.items():
#         if command in phrases:
#             open_application(app_key)
#             return True

#     # Website shortcuts
#     if command.startswith("open "):
#         target = command.removeprefix("open ").strip()

#         if open_website(target):
#             return True

#         # If the target is an unknown site, don't guess or execute it.
#         speak(
#             "I don't recognize that website. "
#             "Try Google, YouTube, Gmail, GitHub, or ChatGPT."
#         )
#         return True

#     # Unknown command
#     speak(
#         "Sorry, I don't understand that command yet. "
#         "Please try another command."
#     )
#     return True


# # ==========================================
# # MAIN PROGRAM
# # ==========================================

# def main():

#     print("=" * 45)
#     print("          Aarvya AI - V2")
#     print("          SMART COMMANDS")
#     print("=" * 45)

#     speak("Hello! Aarvya ru AI version 3 is ready.")

#     while True:
#         command = listen()

#         if not handle_command(command):
#             break


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nAarvya AI stopped by keyboard.")
#     finally:
#         try:
#             engine.stop()
#         except Exception:
#             pass

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8


# ---------- VOICE OUTPUT ----------

def speak(text):
    print(f"\nGuru AI: {text}")

    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as error:
        print("Speech output error:", error)


# ---------- VOICE INPUT ----------

def listen():
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

        print("You:", command)
        return command.lower().strip()

    except sr.WaitTimeoutError:
        print("No speech detected.")

    except sr.UnknownValueError:
        print("Voice was not understood.")

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")

    except OSError:
        speak("Microphone error. Please check your microphone.")

    except Exception as error:
        print("Listening error:", error)

    return ""


# ---------- APPLICATIONS ----------

def open_application(app_name):
    app_commands = {
        "calculator": ["calc.exe"],
        "notepad": ["notepad.exe"],
        "paint": ["mspaint.exe"],
        "wordpad": ["write.exe"],
    }

    if app_name == "chrome":
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
                    pass

        chrome = shutil.which("chrome")

        if chrome:
            try:
                subprocess.Popen([chrome])
                speak("Opening Chrome.")
                return
            except OSError:
                pass

        speak("Chrome was not found on this computer.")
        return

    if app_name == "vs code":
        code_path = shutil.which("code")

        if not code_path:
            possible_paths = [
                Path.home() / "AppData/Local/Programs/Microsoft VS Code/Code.exe",
                Path("C:/Program Files/Microsoft VS Code/Code.exe"),
            ]

            for path in possible_paths:
                if path.is_file():
                    code_path = str(path)
                    break

        if code_path:
            try:
                subprocess.Popen([code_path])
                speak("Opening Visual Studio Code.")
            except OSError:
                speak("Could not open Visual Studio Code.")
        else:
            speak("VS Code was not found.")
        return

    try:
        subprocess.Popen(app_commands[app_name])
        speak(f"Opening {app_name}.")
    except (OSError, KeyError):
        speak(f"Could not open {app_name}.")


# ---------- FOLDERS ----------

def get_folders():
    home = Path.home()

    return {
        "desktop": home / "Desktop",
        "downloads": home / "Downloads",
        "documents": home / "Documents",
        "pictures": home / "Pictures",
        "music": home / "Music",
        "videos": home / "Videos",
    }


def open_folder(folder_name):
    folders = get_folders()
    folder = folders.get(folder_name)

    if folder and folder.is_dir():
        try:
            os.startfile(str(folder))
            speak(f"Opening {folder_name}.")
        except OSError:
            speak("I could not open that folder.")
    else:
        speak(f"The {folder_name} folder was not found.")


# ---------- FILE SEARCH ----------

def search_file(filename):
    filename = filename.strip().strip("\"'")

    if not filename:
        speak("Please tell me the file name.")
        return

    # Search only common user folders.
    # This avoids scanning the entire computer.
    search_folders = [
        Path.home() / "Desktop",
        Path.home() / "Downloads",
        Path.home() / "Documents",
    ]

    results = []
    maximum_results = 10

    speak(f"Searching for {filename}.")

    for folder in search_folders:
        if not folder.is_dir():
            continue

        try:
            for path in folder.rglob("*"):
                if path.is_file() and filename.casefold() in path.name.casefold():
                    results.append(path)

                    if len(results) >= maximum_results:
                        break

        except (OSError, PermissionError):
            continue

        if len(results) >= maximum_results:
            break

    if not results:
        speak("No matching files were found in Desktop, Downloads, or Documents.")
        return

    print("\nMatching files:")

    for index, path in enumerate(results, start=1):
        print(f"{index}. {path}")

    speak(f"I found {len(results)} matching file or files.")

    # Automatically open a file only when there is one exact match.
    exact_matches = [
        path for path in results
        if path.name.casefold() == filename.casefold()
    ]

    if len(exact_matches) == 1:
        speak("I found one exact match. Would you like to open it?")
        answer = listen()

        if any(word in answer for word in ("yes", "open it", "haan", "ha")):
            try:
                os.startfile(str(exact_matches[0]))
                speak("Opening the file.")
            except OSError:
                speak("I could not open that file.")
    else:
        speak("Check the file paths in the terminal to identify the correct file.")


# ---------- SYSTEM INFORMATION ----------

def show_cpu():
    try:
        usage = psutil.cpu_percent(interval=1)
        speak(f"CPU usage is {usage} percent.")
    except Exception as error:
        print("CPU information error:", error)
        speak("I could not read CPU information.")


def show_ram():
    try:
        memory = psutil.virtual_memory()
        used_gb = memory.used / (1024 ** 3)
        total_gb = memory.total / (1024 ** 3)

        speak(
            f"RAM usage is {memory.percent} percent. "
            f"{used_gb:.1f} gigabytes used out of "
            f"{total_gb:.1f} gigabytes."
        )
    except Exception as error:
        print("RAM information error:", error)
        speak("I could not read RAM information.")


def show_battery():
    try:
        battery = psutil.sensors_battery()

        if battery is None:
            speak("Battery information is not available on this device.")
            return

        percentage = round(battery.percent)

        if battery.power_plugged:
            status = "charging or connected to power"
        else:
            status = "running on battery"

        speak(f"Battery is at {percentage} percent and is {status}.")

    except Exception as error:
        print("Battery information error:", error)
        speak("I could not read battery information.")


def show_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()

        print("\n--- SYSTEM INFORMATION ---")
        print(f"CPU usage: {cpu}%")
        print(f"RAM usage: {memory.percent}%")
        print(f"RAM used: {memory.used / (1024 ** 3):.2f} GB")
        print(f"RAM total: {memory.total / (1024 ** 3):.2f} GB")

        battery = psutil.sensors_battery()

        if battery is not None:
            print(f"Battery: {battery.percent}%")
        else:
            print("Battery: Not available")

        speak(
            f"CPU usage is {cpu} percent and RAM usage is "
            f"{memory.percent} percent."
        )

    except Exception as error:
        print("System information error:", error)
        speak("I could not read all system information.")


# ---------- WEB SEARCH ----------

def google_search(query):
    if not query.strip():
        speak("Please tell me what to search.")
        return

    webbrowser.open(
        "https://www.google.com/search?q=" + quote_plus(query)
    )
    speak(f"Searching Google for {query}.")


def youtube_search(query):
    if not query.strip():
        speak("Please tell me what to search.")
        return

    webbrowser.open(
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )
    speak(f"Searching YouTube for {query}.")


def open_website(name):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "gmail": "https://mail.google.com",
        "github": "https://github.com",
        "chatgpt": "https://chatgpt.com",
    }

    if name in websites:
        webbrowser.open(websites[name])
        speak(f"Opening {name}.")
        return True

    return False


# ---------- COMMAND HANDLER ----------

def handle_command(command):
    if not command:
        return True

    # Exit the assistant; does not shut down Windows.
    if command in ("exit", "quit", "stop", "goodbye", "stop guru"):
        speak("Goodbye. Guru AI is stopping.")
        return False

    # Greetings
    if any(word in command for word in (
        "hello", "hi guru", "hey guru",
        "good morning", "good afternoon", "good evening"
    )):
        speak("Hello! I am Guru AI. How can I help you?")
        return True

    # Time and date
    if "time" in command:
        speak(datetime.now().strftime("The time is %I:%M %p."))
        return True

    if "date" in command or "today" in command:
        speak(datetime.now().strftime("Today's date is %d %B %Y."))
        return True

    # System information
    if "system information" in command or "system info" in command:
        show_system_info()
        return True

    if "cpu" in command or "processor usage" in command:
        show_cpu()
        return True

    if "ram" in command or "memory usage" in command:
        show_ram()
        return True

    if "battery" in command:
        show_battery()
        return True

    # File search
    if command.startswith("search file for "):
        search_file(command.removeprefix("search file for "))
        return True

    if command.startswith("search files for "):
        search_file(command.removeprefix("search files for "))
        return True

    if command.startswith("find file "):
        search_file(command.removeprefix("find file "))
        return True

    # Folder commands
    folders = get_folders()

    folder_aliases = {
        "my desktop": "desktop",
        "desktop": "desktop",
        "downloads": "downloads",
        "my downloads": "downloads",
        "documents": "documents",
        "my documents": "documents",
        "pictures": "pictures",
        "music folder": "music",
        "videos folder": "videos",
    }

    if command.startswith("open "):
        target = command.removeprefix("open ").strip()

        if target in folder_aliases:
            open_folder(folder_aliases[target])
            return True

        # Open supported applications
        app_aliases = {
            "calculator": "calculator",
            "notepad": "notepad",
            "paint": "paint",
            "wordpad": "wordpad",
            "chrome": "chrome",
            "vs code": "vs code",
            "vscode": "vs code",
            "visual studio code": "vs code",
        }

        if target in app_aliases:
            open_application(app_aliases[target])
            return True

        # Open supported websites
        if open_website(target):
            return True

        speak(
            "I do not recognize that app, folder, or website. "
            "Please try a supported command."
        )
        return True

    # Search the web
    if command.startswith("search google for "):
        google_search(command.removeprefix("search google for "))
        return True

    if command.startswith("google search "):
        google_search(command.removeprefix("google search "))
        return True

    if command.startswith("search youtube for "):
        youtube_search(command.removeprefix("search youtube for "))
        return True

    if command.startswith("youtube search "):
        youtube_search(command.removeprefix("youtube search "))
        return True

    speak("Sorry, I do not understand that command yet.")
    return True


# ---------- MAIN ----------

def main():
    print("=" * 45)
    print("GURU AI - V4 PC ASSISTANT")
    print("=" * 45)

    speak("Hello! Guru AI version 4 is ready.")

    while True:
        command = listen()

        if not handle_command(command):
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGuru AI stopped by keyboard.")
    finally:
        try:
            engine.stop()
        except Exception:
            pass

