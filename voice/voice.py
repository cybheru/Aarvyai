
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

recognizer = sr.Recognizer()


def speak(text):
    print("Guru AI:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")

        # First try Hindi
        try:
            command = recognizer.recognize_google(
                audio,
                language="hi-IN"
            )
            print("You:", command)
            return command.lower().strip()

        except sr.UnknownValueError:
            pass

        # If Hindi recognition fails, try English
        try:
            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )
            print("You:", command)
            return command.lower().strip()

        except sr.UnknownValueError:
            print("Could not understand your voice.")
            return ""

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""

    except OSError:
        print("Microphone error. Check your microphone.")
        return ""

    except Exception as error:
        print("Voice error:", error)
        return ""
