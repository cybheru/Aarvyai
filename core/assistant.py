"""Voice command routing for Aarvyai."""
from datetime import datetime

from pc.pc_control import (
    open_application,
    open_folder,
    search_file,
    show_battery,
    show_cpu,
    show_ram,
    show_system_info,
)
from web.web_control import (
    google_search,
    github_search,
    open_website,
    wikipedia_search,
    youtube_search,
)


def handle_command(command: str, speak) -> bool:
    """Handle one recognized command. Return False to stop the assistant."""
    command = command.lower().strip()
    if not command:
        return True

    if command in {"exit", "quit", "stop", "goodbye", "stop aarvyai"}:
        speak("Goodbye! Aarvyai is stopping.")
        return False

    if any(phrase in command for phrase in ("hello", "hi aarvyai", "hey aarvyai", "good morning", "good afternoon", "good evening")):
        speak("Hello! I am Aarvyai. How can I help you?")
        return True

    if "time" in command:
        speak(f"The current time is {datetime.now():%I:%M %p}.")
        return True
    if "date" in command or "today" in command:
        speak(f"Today's date is {datetime.now():%d %B %Y}.")
        return True

    if "system information" in command or "system info" in command:
        show_system_info(speak)
        return True
    if "cpu" in command or "processor usage" in command:
        show_cpu(speak)
        return True
    if "ram" in command or "memory usage" in command:
        show_ram(speak)
        return True
    if "battery" in command:
        show_battery(speak)
        return True

    for prefix in ("search files for ", "search file for ", "find file "):
        if command.startswith(prefix):
            search_file(command[len(prefix):].strip(), speak)
            return True

    searches = (
        ("search google for ", google_search),
        ("google search ", google_search),
        ("search youtube for ", youtube_search),
        ("youtube search ", youtube_search),
        ("search github for ", github_search),
        ("search wikipedia for ", wikipedia_search),
    )
    for prefix, search in searches:
        if command.startswith(prefix):
            speak(search(command[len(prefix):].strip()))
            return True

    if command.startswith("open "):
        target = command.removeprefix("open ").strip()
        folders = {
            "desktop": "desktop", "my desktop": "desktop",
            "downloads": "downloads", "my downloads": "downloads",
            "documents": "documents", "my documents": "documents",
            "pictures": "pictures", "music": "music", "videos": "videos",
        }
        if target in folders:
            open_folder(folders[target], speak)
            return True

        applications = {
            "calculator": "calculator", "notepad": "notepad",
            "paint": "paint", "chrome": "chrome",
            "vs code": "vs code", "vscode": "vs code",
            "visual studio code": "vs code",
        }
        if target in applications:
            open_application(applications[target], speak)
            return True

        result = open_website(target)
        speak(result)
        return True

    speak("Sorry, I did not understand that command.")
    return True
