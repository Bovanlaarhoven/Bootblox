import os
import shutil

Roblox = "/Applications/Roblox.app"
ClientSettings = Roblox + "/Contents/MacOS/ClientSettings"
ClientSettingsFile = ClientSettings + "/ClientAppSettings.json"

def check():
    if os.path.exists(ClientSettings):
        print("ClientSettings Found")
        print("Deleting Folder...")
        shutil.rmtree(ClientSettings)
        print("Creating Folder...")
        os.makedirs(ClientSettings, exist_ok=True)
        print("Creating File...")
        with open(ClientSettingsFile, "w") as f:
            f.write("{}")
    else:
        print("ClientSettings Not Found")
        print("Creating Folder...")
        os.makedirs(ClientSettings, exist_ok=True)
        print("Creating File...")
        with open(ClientSettingsFile, "w") as f:
            f.write("{}")
