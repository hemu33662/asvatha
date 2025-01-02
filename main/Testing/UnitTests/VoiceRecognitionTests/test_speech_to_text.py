import sys
import os
import unittest

# Add the root directory of the project to the Python path
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..'))
sys.path.insert(0, root_path)

# Debugging: Print the sys.path to ensure the root path is included
print("Python Path:", sys.path)

from Core.VoiceRecognition.speech_to_text import convert_speech_to_text

class TestSpeechToText(unittest.TestCase):
    def test_speech_to_text(self):
        result = convert_speech_to_text()  # Mock the microphone input for testing
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
