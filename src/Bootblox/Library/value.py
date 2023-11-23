import json

Roblox = "/Applications/Roblox.app"
ClientSettings = Roblox + "/Contents/MacOS/ClientSettings"
ClientSettingsFile = ClientSettings + "/ClientAppSettings.json"

def fps(value):
    with open(ClientSettingsFile, "r") as f:
        settings = json.load(f)

    settings["DFIntTaskSchedulerTargetFps"] = value

    with open(ClientSettingsFile, "w") as f:
        json.dump(settings, f, indent=2)

fps(60)