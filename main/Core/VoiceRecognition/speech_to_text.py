import speech_recognition as sr

class ConvertSpeechToText:
    def __init__(self, command_executor):
        self.command_executor = command_executor
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()


    # def listen_and_recognize(self):
    #     """
    #     Listens to audio input from the microphone and converts it to text.
    #     :param timeout: Maximum duration to listen for input.
    #     :return: Recognized text or None if an error occurs.
    #     """
    #     with sr.Microphone() as source:
    #         print("Listening...")
    #         try:
    #             audio = self.recognizer.listen(source, timeout=20)
    #             text = self.recognizer.recognize_google(audio)
    #             print(f"Recognized: {text}")
    #             return text.lower()
    #         except sr.UnknownValueError:
    #             print("Sorry, could not understand the audio.")
    #         except sr.RequestError as e:
    #             print(f"Could not request results; {e}")
    #         except Exception as e:
    #             print(f"Unexpected error: {e}")
    #     return None
    
    
    def listen_and_recognize(self):
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=20)
            return self.recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("Timeout occurred while listening.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
        # except KeyboardInterrupt:
        #     print("Listening interrupted.")
        #     return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    