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

def lighting(value):
    Lighting = {
        "Voxel": "DFFlagDebugRenderForceTechnologyVoxel",
        "ShadowMap": "FFlagDebugForceFutureIsBrightPhase2",
        "Future": "FFlagDebugForceFutureIsBrightPhase3",
        "None": ""
    }

    key = Lighting.get(value)

    current_value = get_value(key, default=False)


    if current_value is not None:
        for k, v in Lighting.items():
            if k != value:
                set_value(v, False)

        set_value(key, True)
    else:
        default_value = False 
        set_value(key, default_value)
        print(f"Added {key} with default value {default_value} to the settings file.")

def rendering(value):
    Rendering = {
        "Direct3D11": "FFlagDebugGraphicsPreferD3D11",
        "Direct3DFL10": "FFlagDebugGraphicsPreferD3D11FL10",
        "OpenGL": "FFlagDebugGraphicsPreferOpenGL",
        "Metal": "FFlagDebugGraphicsPreferMetal",
        "Vulkan": "FFlagDebugGraphicsPreferVulkan",
        "None": ""
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


