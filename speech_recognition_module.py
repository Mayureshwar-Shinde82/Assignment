import speech_recognition as sr

def speech_to_text():
    """Converts spoken words into text using speech recognition."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Say something...")
        try:
            audio = recognizer.listen(source)
            print("Processing audio...")
        except Exception as e:
            print(f"Error capturing audio: {e}")
            return None

    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# speech_to_text()