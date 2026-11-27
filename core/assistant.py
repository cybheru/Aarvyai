"""Voice command routing for Aarvyai (English and Hindi/Hinglish)."""
from datetime import datetime
import re

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

# Normalize common Roman Hindi/Hinglish control words while keeping the
# original English command patterns intact.
_HINGLISH_REPLACEMENTS = (
    (r"\b(khol do|kholna|kholo|khol)\b", "open"),
    (r"\b(chalao|start karo|shuru karo)\b", "open"),
    (r"\b(dikhao|batao|btao|batana)\b", "show"),
    (r"\b(search karo|dhundo|dhoondo|talash karo)\b", "search"),
    (r"\b(ke liye|ke baare mein|ka)\b", "for"),
    (r"\b(mera|meri|mere)\b", "my"),
    (r"\b(aaj ki|aaj ka|aaj)\b", "today"),
    (r"\b(kya hai|kya hua hai|kitna hai|kitni hai)\b", ""),
    (r"\b(abhi)\b", ""),
)

def _normalize_command(command: str) -> str:
    text = command.lower().strip()
    for pattern, replacement in _HINGLISH_REPLACEMENTS:
        text = re.sub(pattern, replacement, text)
    return re.sub(r"\s+", " ", text).strip(" ,.!?")

def handle_command(command: str, speak) -> bool:
    """Handle one recognized command. Return False to stop the assistant."""
    command = _normalize_command(command)
    if not command:
        return True

    if command in {"exit", "quit", "stop", "goodbye", "stop aarvyai", "band karo", "aarvyai band karo"}:
        speak("Goodbye! Aarvyai is stopping.")
        return False

    if any(phrase in command for phrase in ("hello", "hi aarvyai", "hey aarvyai", "good morning", "good afternoon", "good evening", "namaste", "namaskar", "kaise ho")):
        speak("Namaste! I am Aarvyai. Main aapki kya madad kar sakti hoon?")
        return True

    if "time" in command or "samay" in command or "kitne baje" in command:
        speak(f"The current time is {datetime.now():%I:%M %p}.")
        return True
    if "date" in command or "today" in command or "tarikh" in command or "tareekh" in command:
        speak(f"Today's date is {datetime.now():%d %B %Y}.")
        return True

    if "system information" in command or "system info" in command or "system jankari" in command:
        show_system_info(speak)
        return True
    if "cpu" in command or "processor usage" in command:
        show_cpu(speak)
        return True
    if "ram" in command or "memory usage" in command:
        show_ram(speak)
        return True
    if "battery" in command or "batteri" in command:
        show_battery(speak)
        return True

    for prefix in ("search files for ", "search file for ", "find file ", "file search for "):
        if command.startswith(prefix):
            search_file(command[len(prefix):].strip(), speak)
            return True

    searches = (
        ("search google for ", google_search),
        ("google search ", google_search),
        ("google par search ", google_search),
        ("search youtube for ", youtube_search),
        ("youtube search ", youtube_search),
        ("youtube par search ", youtube_search),
        ("search github for ", github_search),
        ("github par search ", github_search),
        ("search wikipedia for ", wikipedia_search),
        ("wikipedia par search ", wikipedia_search),
    )
    for prefix, search in searches:
        if command.startswith(prefix):
            speak(search(command[len(prefix):].strip()))
            return True

    if command.startswith("search for "):
        speak(google_search(command[len("search for "):].strip()))
        return True

    if command.startswith("open "):
        target = command.removeprefix("open ").strip()
        folders = {
            "desktop": "desktop", "my desktop": "desktop",
            "downloads": "downloads", "my downloads": "downloads",
            "documents": "documents", "my documents": "documents",
            "pictures": "pictures", "music": "music", "videos": "videos",
        }
        # Common Hindi folder names after normalization.
        folders.update({"download folder": "downloads", "document folder": "documents"})
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

    speak("Maaf kijiye, command samajh nahi aaya. Kripya dobara boliye.")
    return True
