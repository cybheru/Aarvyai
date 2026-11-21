"""Speech recognition and speech synthesis."""
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.8


def speak(text: str) -> None:
    print(f"\nAarvyai: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as error:
        print(f"Speech output error: {error}")


def listen() -> str:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You: {command}")
        return command.lower().strip()
    except sr.WaitTimeoutError:
        print("No speech detected.")
    except sr.UnknownValueError:
        print("Voice was not understood.")
    except sr.RequestError:
        speak("Speech recognition service is unavailable. Check your internet connection.")
    except OSError:
        speak("Microphone error. Please check microphone access and connection.")
    except Exception as error:
        print(f"Listening error: {error}")
    return ""


def stop_speech_engine() -> None:
    try:
        engine.stop()
    except Exception:
        pass
