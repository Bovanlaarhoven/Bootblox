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

def rendering(value):
    Rendering = {
        "Direct3D11": "FFlagDebugGraphicsPreferD3D11",
        "Direct3DFL10": "FFlagDebugGraphicsPreferD3D11FL10",
        "OpenGL": "FFlagDebugGraphicsPreferOpenGL",
        "Metal": "FFlagDebugGraphicsPreferMetal",
        "Vulkan": "FFlagDebugGraphicsPreferVulkan"
    }

    key = Rendering.get(value)

    with open(ClientSettingsFile, "r") as f:
        settings = json.load(f)

    for k, v in settings.items():
        if k.startswith("FFlagDebugGraphicsPrefer") and k != key:
            settings[k] = False

    settings[key] = True

    with open(ClientSettingsFile, "w") as f:
        json.dump(settings, f, indent=2)

