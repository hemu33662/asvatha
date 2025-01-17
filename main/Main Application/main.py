# import sys
# import os

# # Add the root directory of the project to the system path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

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

# # Command handler functions
# def handle_open(command):
#     print(f"handle_open received command: {command}")  # Debugging
#     app_name = command.strip().lower()
#     if app_name:
#         if "note" in app_name:  # Flexible for "notepad"
#             app_name = "notepad"
#         elif "paint" in app_name:  # Flexible for "paint" or "mspaint"
#             app_name = "mspaint"
#         elif "browser" in app_name:  # Example: open browser
#             app_name = "chrome"
#         task_queue.add_task({"action": "open", "target": app_name})
#         print(f"Task added to open: {app_name}")
#     else:
#         print("No application name specified after 'open'. Please try again.")

# def handle_system_restart(command):
#     print(f"handle_system_command received command: {command}")  # Debugging
#     command = command.strip().lower()
#     if command:
#         if "pc" in command: 
#             command = "system"
#         elif "laptop" in command: 
#             command = "system"
#         elif "device" in command:  
#             command = "system"
#         task_queue.add_task({"action": "restart", "target": command})
#         print("Task added to restart the system.")
#     else:
#         print("No idea which one to restart.")

# def handle_system_shutdown(command):
#     print(f"handle_system_command received command: {command}")  # Debugging
#     command = command.strip().lower()
#     if command:
#         if "pc" in command: 
#             command = "system"
#         elif "laptop" in command: 
#             command = "system"
#         elif "device" in command:  
#             command = "system"
#         task_queue.add_task({"action": "shutdown", "target": command})
#         print("Task added to shutdown the system.")
#     else:
#         print("No idea which one to shutdown.")

# def handle_search(command):
#     print(f"handle_search received command: {command}")  # Debugging
#     query = command.strip()
#     if query:  # If there's a search query
#         task_queue.add_task({"action": "search", "target": query})
#         print(f"Task added to search for: {query}")
#     else:
#         print("No search query specified. Please provide something to search for.")

# # Register command handlers
# command_parser.register_command("open", handle_open)
# command_parser.register_command("shutdown", handle_system_shutdown)
# command_parser.register_command("restart", handle_system_restart)
# command_parser.register_command("search", handle_search)

# # Main application loop
# def main():
#     print("Asvatha is ready to assist. Say something!")
#     while True:
#         text = speech_to_text.listen_and_recognize()
#         print(f"Recognized: {text}")  # Debugging the recognized text
#         if text:
#             command_parser.parse(text)
            
#             # Process tasks from the task queue
#             while True:
#                 task = task_queue.process_task()
#                 if not task:
#                     break
#                 if not error_detector.detect_error(task):
#                     execute_task(task)
#                 else:
#                     print("Error detected in task execution.")
#         else:
#             print("No command recognized. Please try again.")

# if __name__ == "__main__":
#     main()
