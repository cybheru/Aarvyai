"""Windows application, folder, file and system controls."""
import os
import shutil
import subprocess
from pathlib import Path

try:
    import psutil
except ImportError:
    psutil = None


def open_application(app_name: str, speak) -> None:
    commands = {
        "calculator": ["calc.exe"],
        "notepad": ["notepad.exe"],
        "paint": ["mspaint.exe"],
    }
    if app_name == "chrome":
        candidates = [
            Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
            Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
            Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe",
        ]
        executable = next((str(p) for p in candidates if p.is_file()), None) or shutil.which("chrome")
        if not executable:
            speak("Chrome was not found on this computer.")
            return
        command = [executable]
    elif app_name == "vs code":
        executable = shutil.which("code")
        if not executable:
            candidates = [
                Path.home() / "AppData/Local/Programs/Microsoft VS Code/Code.exe",
                Path("C:/Program Files/Microsoft VS Code/Code.exe"),
            ]
            executable = next((str(p) for p in candidates if p.is_file()), None)
        if not executable:
            speak("Visual Studio Code was not found on this computer.")
            return
        command = [executable]
    else:
        command = commands.get(app_name)
        if command is None:
            speak("That application is not supported.")
            return
    try:
        subprocess.Popen(command)
        speak(f"Opening {app_name}.")
    except OSError:
        speak(f"Could not open {app_name}.")


def open_folder(folder_name: str, speak) -> None:
    folders = {
        name: Path.home() / name.title()
        for name in ("desktop", "downloads", "documents", "pictures", "music", "videos")
    }
    folder = folders.get(folder_name)
    if not folder or not folder.is_dir():
        speak(f"The {folder_name} folder was not found.")
        return
    try:
        os.startfile(str(folder))
        speak(f"Opening {folder_name}.")
    except (AttributeError, OSError):
        speak("I could not open that folder on this operating system.")


def search_file(filename: str, speak) -> None:
    filename = filename.strip().strip("\"'")
    if not filename:
        speak("Please tell me the file name.")
        return
    locations = [Path.home() / name for name in ("Desktop", "Downloads", "Documents")]
    matches = []
    for location in locations:
        if not location.is_dir():
            continue
        try:
            for item in location.rglob("*"):
                try:
                    if item.is_file() and filename.casefold() in item.name.casefold():
                        matches.append(item)
                        if len(matches) >= 10:
                            break
                except OSError:
                    continue
        except OSError:
            continue
        if len(matches) >= 10:
            break
    if not matches:
        speak("No matching files were found in Desktop, Downloads, or Documents.")
        return
    print("\nMatching files:")
    for index, item in enumerate(matches, start=1):
        print(f"{index}. {item}")
    exact = [item for item in matches if item.name.casefold() == filename.casefold()]
    if len(exact) == 1:
        speak("I found one exact match. Its path is shown in the terminal; no file was opened.")
        print(f"Exact match: {exact[0]}")
    else:
        speak(f"I found {len(matches)} matching files. Check the paths in the terminal.")


def _require_psutil(speak) -> bool:
    if psutil is None:
        speak("System monitoring is unavailable. Install the project requirements first.")
        return False
    return True


def show_cpu(speak) -> None:
    if _require_psutil(speak):
        speak(f"CPU usage is {psutil.cpu_percent(interval=1)} percent.")


def show_ram(speak) -> None:
    if _require_psutil(speak):
        memory = psutil.virtual_memory()
        used = memory.used / (1024 ** 3)
        total = memory.total / (1024 ** 3)
        speak(f"RAM usage is {memory.percent} percent, {used:.1f} of {total:.1f} gigabytes.")


def show_battery(speak) -> None:
    if not _require_psutil(speak):
        return
    battery = psutil.sensors_battery()
    if battery is None:
        speak("Battery information is not available on this device.")
        return
    status = "connected to power" if battery.power_plugged else "running on battery"
    speak(f"Battery is at {round(battery.percent)} percent and is {status}.")


def show_system_info(speak) -> None:
    if not _require_psutil(speak):
        return
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    battery = psutil.sensors_battery()
    battery_text = f"{round(battery.percent)} percent" if battery else "not available"
    speak(
        f"CPU usage is {cpu} percent. RAM usage is {memory.percent} percent, "
        f"{memory.used / (1024 ** 3):.1f} of {memory.total / (1024 ** 3):.1f} gigabytes. "
        f"Battery is {battery_text}."
    )
