# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

# # Print sys.path for debugging
# print("sys.path:", sys.path)

# from Core.VoiceRecognition.speech_to_text import ConvertSpeechToText
# from Core.VoiceRecognition.command_parser import CommandParser
# from Core.TaskManagement.task_queue import TaskQueue
# from Core.TaskManagement.task_executor import execute_task
# from Core.ErrorHandling.error_detection import ErrorDetection

# # Initialize components
# speech_to_text = ConvertSpeechToText(command_executor=execute_task)
# command_parser = CommandParser()
# task_queue = TaskQueue()
# error_detector = ErrorDetection()

# # Register command handlers
# def handle_open(command):
#     app_name = command.split("open", 1)[1].strip()
#     task_queue.add_task({"action": "open", "target": app_name})

# def handle_system_command(command):
#     task_queue.add_task({"action": "system", "target": command})

# command_parser.register_command("open", handle_open)
# command_parser.register_command("shutdown", handle_system_command)
# command_parser.register_command("restart", handle_system_command)

# # Main application loop
# def main():
#     print("Asvatha is ready to assist. Say something!")
#     while True:
#         text = speech_to_text.convert_speech_to_text()
#         if text:
#             command_parser.parse(text)
#             while True:
#                 task = task_queue.process_task()
#                 if not task:
#                     break
#                 if not error_detector.detect_error(task):
#                     execute_task(task)

# if __name__ == "__main__":
#     main()
