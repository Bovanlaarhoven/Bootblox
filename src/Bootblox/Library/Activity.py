import os
import requests

logspath = "~/Library/Logs/Roblox"

def get_latest_log(search_string):
    logspath_expanded = os.path.expanduser(logspath)

    all_files = os.listdir(logspath_expanded)

    log_files = [file for file in all_files if file.endswith(".log")]

    sorted_files = sorted(log_files, key=lambda x: os.path.getmtime(os.path.join(logspath_expanded, x)), reverse=True)
    for filename in sorted_files:
        file_path = os.path.join(logspath_expanded, filename)
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as file:
                log_data = file.readlines()
                for entry in reversed(log_data):
                    if search_string in entry:
                        return entry.strip()
        except UnicodeDecodeError:
            print(f"Error decoding file: {file_path}")

    return None 

def get_game_id():
    search = "[FLog::Output] ! Joining game"
    latest_log_entry = get_latest_log(search)
    return latest_log_entry.split(" ")[-3]

def get_server_location_info():
    search = "[FLog::Network] serverId:"
    latest_log_entry = get_latest_log(search)

    if latest_log_entry:
        server_location = latest_log_entry.split(search)[1].split("|")[0].strip()
        
        city_url = f"https://ipinfo.io/{server_location}/city"
        region_url = f"https://ipinfo.io/{server_location}/region"
        country_url = f"https://ipinfo.io/{server_location}/country"

        city_response = requests.get(city_url)
        region_response = requests.get(region_url)
        country_response = requests.get(country_url)

        if all(response.status_code == 200 for response in [city_response, region_response, country_response]):
            return {
                "city": city_response.text.strip(),
                "region": region_response.text.strip(),
                "country": country_response.text.strip(),
            }
        else:
            print("Failed to retrieve location information.")
    
    return None

def check_activity():
    join = "[FLog::Output] ! Joining game"
    leave = "[FLog::Network] Time to disconnect replication data"

    join_logs = get_latest_log(join)
    leave_logs = get_latest_log(leave)

    if leave_logs and join_logs:
        if leave_logs > join_logs:
            return "You are not in a game."
        else:
            game_id = get_game_id()
            location_info = get_server_location_info()
            if location_info:
                return f"You are in a game. Game ID: {game_id}\nServer Location: {location_info['city']}, {location_info['region']}, {location_info['country']}"
            else:
                return "Failed to retrieve server location information."
    elif join_logs:
        game_id = get_game_id()
        location_info = get_server_location_info()
        if location_info:
            return f"You are in a game. Game ID: {game_id}\nServer Location: {location_info['city']}, {location_info['region']}, {location_info['country']}"
        else:
            return "Failed to retrieve server location information."
    else:
        return "No relevant logs found."

def send_notification(mode, data=None):
    title = "Roblox Notification"
    message = ""
    
    if mode == "ServerInfo":
        if data:
            message = f"Server Location: {data['city']}, {data['region']}, {data['country']}"
        else:
            message = "Failed to retrieve server location information."
    
    elif mode == "GameInfo":
        if data:
            message = f"You are in a game. Game ID: {data['game_id']}"
            location_info = get_server_location_info()
            if location_info:
                message += f"\nServer Location: {location_info['city']}, {location_info['region']}, {location_info['country']}"
            else:
                message += "\nFailed to retrieve server location information."
        else:
            message = "You are not in a game."

    os.system(f"osascript -e 'display notification \"{message}\" with title \"{title}\"'")

