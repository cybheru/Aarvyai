"""Aarvyai V5: modular Windows voice assistant."""
from core.assistant import handle_command
from voice.voice import listen, speak, stop_speech_engine


def main() -> None:
    print("=" * 45)
    print("AARVYAI V5 - WINDOWS VOICE ASSISTANT")
    print("=" * 45)
    speak("Hello! Aarvyai version 5 is ready.")

    try:
        while handle_command(listen(), speak):
            pass
    except KeyboardInterrupt:
        print("\nAarvyai stopped by keyboard.")
    finally:
        stop_speech_engine()


if __name__ == "__main__":
    main()
