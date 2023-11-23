import os
import json

Roblox = "/Applications/Roblox.app"
ClientSettings = os.path.join(Roblox, "Contents/MacOS/ClientSettings")
ClientSettingsFile = os.path.join(ClientSettings, "ClientAppSettings.json")

with open(ClientSettingsFile) as f:
    data = json.load(f)

# Access the value
value = data['key']  # Replace 'key' with the actual key in your JSON file
print(value)
