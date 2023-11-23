import json

Roblox = "/Applications/Roblox.app"
ClientSettings = Roblox + "/Contents/MacOS/ClientSettings"
ClientSettingsFile = ClientSettings + "/ClientAppSettings.json"

def get_value(key, default=None):
    try:
        with open(ClientSettingsFile, "r") as f:
            data = json.load(f)
        return data.get(key, default)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

    
def set_value(key, value):
    with open(ClientSettingsFile, "r") as f:
        data = json.load(f)
        data[key] = value
    with open(ClientSettingsFile, "w") as f:
        json.dump(data, f, indent=4)

    