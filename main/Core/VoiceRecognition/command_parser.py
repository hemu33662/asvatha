def parse_command(command):
    # Basic command parsing logic
    if "open" in command:
        app_name = command.replace("open", "").strip()
        return {"action": "open", "target": app_name}
    elif "search" in command:
        query = command.replace("search", "").strip()
        return {"action": "search", "target": query}
    else:
        return {"action": "unknown", "target": command}
