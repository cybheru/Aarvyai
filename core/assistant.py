
import datetime
import re

from web.web_control import (
    open_website,
    google_search,
    youtube_search,
    github_search,
    wikipedia_search
)

from pc.pc_control import (
    open_application,
    open_folder,
    search_file,
    show_cpu,
    show_ram,
    show_battery,
    show_system_info
)


def clean_command(command):
    command = command.lower().strip()
    command = re.sub(r"[^\w\s]", "", command)
    command = re.sub(r"\s+", " ", command)
    return command


def handle_command(command, speak):

    command = clean_command(command)

    if not command:
        return True

    # -------------------------
    # EXIT COMMANDS
    # -------------------------

    exit_commands = [
        "exit", "quit", "stop", "goodbye",
        "बंद हो जाओ", "बंद करो", "रुक जाओ",
        "गुरु बंद हो जाओ", "गुरु रुक जाओ"
    ]

    if command in exit_commands:
        speak("Goodbye! Guru AI is shutting down.")
        return False

    # -------------------------
    # GREETING
    # -------------------------

    greetings = [
        "hello", "hi", "hey guru",
        "नमस्ते", "नमस्कार", "हेलो",
        "हाय गुरु", "नमस्ते गुरु"
    ]

    if command in greetings:
        speak("Hello! Namaste. How can I help you?")
        return True

    # -------------------------
    # TIME
    # -------------------------

    time_commands = [
        "time", "what is the time",
        "समय बताओ", "टाइम बताओ",
        "अभी कितना समय हुआ है"
    ]

    if command in time_commands or "time batao" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return True

    # -------------------------
    # DATE
    # -------------------------

    date_commands = [
        "date", "today date",
        "आज की तारीख बताओ", "तारीख बताओ",
        "आज कौन सी तारीख है"
    ]

    if command in date_commands or "date batao" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}.")
        return True

    # -------------------------
    # SYSTEM INFORMATION
    # -------------------------

    if "system information" in command or "system info" in command:
        show_system_info(speak)
        return True

    if "सिस्टम जानकारी" in command or "system ki jankari" in command:
        show_system_info(speak)
        return True

    if "cpu" in command or "सीपीयू" in command:
        show_cpu(speak)
        return True

    if "ram" in command or "रैम" in command:
        show_ram(speak)
        return True

    if "battery" in command or "बैटरी" in command:
        show_battery(speak)
        return True

    # -------------------------
    # FILE SEARCH
    # -------------------------

    file_prefixes = [
        "search file for ",
        "find file ",
        "file search ",
        "file dhundo ",
        "फाइल ढूंढो ",
        "फाइल खोजो ",
        "open ",
        "kholo ",
        "khol do ",
        "खोलो ",
        "खोल दो ",
        "ओपन "
    ]   

    for prefix in file_prefixes:
        if command.startswith(prefix):
            filename = command[len(prefix):].strip()

            if filename:
                search_file(filename, speak)
            else:
                speak("Please tell me the file name.")

            return True

    # -------------------------
    # WEB SEARCH
    # -------------------------

    search_patterns = [
        ("search google for ", google_search),
        ("google par search karo ", google_search),
        ("google pe search karo ", google_search),
        ("google par search karo ", google_search),
        ("गूगल पर सर्च करो ", google_search),
        ("गूगल पर खोजो ", google_search),

        ("search youtube for ", youtube_search),
        ("youtube par search karo ", youtube_search),
        ("youtube pe search karo ", youtube_search),
        ("यूट्यूब पर सर्च करो ", youtube_search),

        ("search github for ", github_search),
        ("github par search karo ", github_search),
        ("गिटहब पर सर्च करो ", github_search),

        ("search wikipedia for ", wikipedia_search),
        ("wikipedia par search karo ", wikipedia_search),
        ("विकिपीडिया पर खोजो ", wikipedia_search)
    ]

    for prefix, search_function in search_patterns:
        if command.startswith(prefix):
            query = command[len(prefix):].strip()

            if query:
                speak(search_function(query))
            else:
                speak("Please tell me what to search.")

            return True

    # -------------------------
    # OPEN APPLICATIONS
    # -------------------------

    app_commands = {
        "calculator": [
            "open calculator",
            "calculator kholo",
            "calculator khol do",
            "कैलकुलेटर खोलो",
            "कैलकुलेटर खोल दो"
        ],

        "notepad": [
            "open notepad",
            "notepad kholo",
            "notepad khol do",
            "नोटपैड खोलो"
        ],

        "paint": [
            "open paint",
            "paint kholo",
            "पेंट खोलो"
        ],

        "chrome": [
            "open chrome",
            "chrome kholo",
            "क्रोम खोलो"
        ],

        "vs code": [
            "open vs code",
            "open visual studio code",
            "vs code kholo",
            "वीएस कोड खोलो"
        ]
    }

    for app, phrases in app_commands.items():
        if command in phrases:
            open_application(app, speak)
            return True

    # -------------------------
    # OPEN FOLDERS
    # -------------------------

    folder_commands = {
        "desktop": [
            "open desktop",
            "desktop kholo",
            "डेस्कटॉप खोलो"
        ],

        "downloads": [
            "open downloads",
            "downloads kholo",
            "डाउनलोड खोलो",
            "डाउनलोड्स खोलो"
        ],

        "documents": [
            "open documents",
            "documents kholo",
            "डॉक्यूमेंट खोलो",
            "डॉक्यूमेंट्स खोलो"
        ],

        "pictures": [
            "open pictures",
            "pictures kholo",
            "फोटो फोल्डर खोलो",
            "पिक्चर्स खोलो"
        ]
    }

    for folder, phrases in folder_commands.items():
        if command in phrases:
            open_folder(folder, speak)
            return True

    # -------------------------
    # OPEN WEBSITES
    # -------------------------

    website_aliases = {
        "गूगल": "google",
        "यूट्यूब": "youtube",
        "जीमेल": "gmail",
        "गिटहब": "github",
        "लिंक्डइन": "linkedin",
        "विकिपीडिया": "wikipedia",
        "चैट जीपीटी": "chatgpt",
        "यूट्यूब खोलो": "youtube",
        "गूगल खोलो": "google",
        "जीमेल खोलो": "gmail",
        "गिटहब खोलो": "github",
        "ओपन यूट्यूब": "youtube",
        "ओपन गूगल": "google",
        "ओपन जीमेल": "gmail"
    }

    open_prefixes = [
        "open ",
        "kholo ",
        "khol do ",
        "खोलो ",
        "खोल दो "
    ]

    for prefix in open_prefixes:
        if command.startswith(prefix):
            target = command[len(prefix):].strip()
            target = website_aliases.get(target, target)

            result = open_website(target)
            speak(result)
            return True

    # -------------------------
    # UNKNOWN COMMAND
    # -------------------------

    speak("Sorry, I did not understand. Please try another command.")
    return True
