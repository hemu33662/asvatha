from Core.VoiceRecognition.speech_to_text import convert_speech_to_text
from Core.VoiceRecognition.command_parser import parse_command
from Core.CommandExecutor.system_commands import execute_command

def main():
    print("Asvatha is running...")
    while True:
        print("\nSay a command:")
        text = convert_speech_to_text()
        if text:
            parsed_command = parse_command(text)
            execute_command(parsed_command)

if __name__ == "__main__":
    main()
