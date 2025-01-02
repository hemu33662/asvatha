import speech_recognition as sr

def convert_speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        return None
