try:
    import speech_recognition as sr  # type: ignore[import-not-found]
except ImportError:
    sr = None

try:
    import pyttsx3  # type: ignore[import-not-found]
except ImportError:
    pyttsx3 = None
import webbrowser
from datetime import datetime

from click import command

# ----------------------
# Text-to-speech setup

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print(f"Aarvyai AI: {text}")
    engine.say(text)
    engine.runAndWait()


# ----------------------
# Speech recognition setup
# ----------------------
recogniser = sr.Recognizer()


def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening...")

            
            recogniser.adjust_for_ambient_noise(
                 source, duration=0.5
            )

            audio = recogniser.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")
        text = recogniser.recognize_google(audio)
        print(f"You: {command}")

        return command.lower().strip()


    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        return ""
    except sr.RequestError:
        print("Speech recogniser service is unavailable.")
        return ""
    except OSError:
        print("Microphone error. Please check your microphone.")
        return ""
    except Exception as error:
        print(f"Unexpected error: {error}")

        return ""


# ----------------------------
# command handling
# ----------------------------

def handle_command(command):
    

    if not command:
         return True

    #Greeting
    if any(word in command for word in [
        "hello", "hi arvyai", "hey", "good morning",
        "good afternoon", "good evening", "good night"
    ]):
        speak("Hello! I am Aarvyai AI. How can I help you today?")
#time
    elif "time" in command:
         current_time = datetime.now().strftime("%I:%M %p")       
         speak(f"The current time is {current_time}")

         #date
    elif "date" in command or "today" in command:
         current_date = datetime.now().strftime("%B %d, %Y")
         speak(f"Today's date is {current_date}")

    #Open Google
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open("http://www.google.com")
    #Open Youtube
    elif "open youtube" in command:
        speak("Opening Youtube.")
        webbrowser.open("http://www.youtube.com")
    #Open Whatsapp
    elif "open whatsapp" in command:
        speak("Opening Whatsapp.")
        webbrowser.open("http://www.whatsapp.com")
    # Exit
    elif any(word in command for word in [
         "stop", "exit", "quit"
         ]):
        speak("Goodbye! Aarvyai AI is shutting down.")

        return False
    else:
         speak("Sorry , I do not know that command yet.")


    return True

#----------------------------
#Main Program
#----------------------------

def main():
    print("=" * 40)
    print("   Aarvya AI")
    print("      basic Voice Assistant ")
    print("_" * 40)

    speak("Hello I am Aarvyai AI. I am ready.")

    while True:
        command = listen()

        if not handle_command(command):
            break


# ----------------------------
# Program Entry Point
if __name__ == "__main__":
    try:
        main() 
    except KeyboardInterrupt:
        print("\nAarvyai AI stopped by keyboard.")
