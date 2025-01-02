import os
import webbrowser

def execute_command(parsed_command):
    action = parsed_command.get("action")
    target = parsed_command.get("target")

    if action == "open":
        print(f"Opening {target}...")
        os.system(f"start {target}")  # Adjust for Linux/macOS with 'open'
    elif action == "search":
        print(f"Searching for {target}...")
        webbrowser.open(f"https://www.google.com/search?q={target}")
    else:
        print(f"Unknown command: {target}")
