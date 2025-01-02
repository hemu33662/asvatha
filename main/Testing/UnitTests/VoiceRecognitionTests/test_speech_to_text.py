import sys
import os
import unittest

# Add the Asvatha root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Core.VoiceRecognition.speech_to_text import convert_speech_to_text

class TestSpeechToText(unittest.TestCase):
    def test_speech_to_text(self):
        result = convert_speech_to_text()  # Mock the microphone input for testing
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
