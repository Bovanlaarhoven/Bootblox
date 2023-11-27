import sys
import os
import tkinter as tk
from tkinter import ttk

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.input import rendering
from Library.input import lighting
from Library.input import set_value
from Library.check import check
from Library.Activity import send_notification
from Library.Activity import check_activity
from Library.Activity import get_latest_log
from Library.Activity import get_game_id
from Library.Activity import get_server_location_info

def set_fps(event):
    value = framerate.get()
    try:
        value = int(value)
        set_value("DFIntTaskSchedulerTargetFps", value)
    except ValueError:
        print("Invalid input. Please enter a valid integer for FPS.")


def set_notifcation_mode(*args):
    value = notifcation_mode.get()
    if value == "GameInfo":
        send_notification("GameInfo", {"game_id": get_game_id()})
    elif value == "ServerInfo":
        send_notification("ServerInfo", get_server_location_info())

notification_sent = False

def toggle_notification():
    global notification_sent
    value = notification_var.get()
    join = "[FLog::Output] ! Joining game"
    leave = "[FLog::Network] Time to disconnect replication data"

    join_logs = get_latest_log(join)
    leave_logs = get_latest_log(leave)

    if value and join_logs and (not notification_sent):
        send_notification("GameInfo", {"game_id": get_game_id()})
        notification_sent = True
    elif not value or not join_logs:
        notification_sent = False


def set_rendering(*args):
    value = rendering_mode.get()
    rendering(value)

def set_lighting(*args):
    value = lighting_mode.get()
    lighting(value)

def create_tab(tab_name, content):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)

    label_frame = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
    label_frame.pack(fill="x", pady=1)

    label = tk.Label(label_frame, text=content, anchor=tk.W)
    label.pack(fill="x")

    if tab_name == "FastFlags":
        frame1 = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
        frame2 = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
        frame3 = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
        frame1.pack(fill="x", pady=5)
        frame2.pack(fill="x", pady=5)
        frame3.pack(fill="x", pady=5)

        label_input = tk.Label(frame1, text="Framerate limit:", anchor=tk.W)
        label_input.pack(side="left")
        label_rendering = tk.Label(frame2, text="Rendering:", anchor=tk.W)
        label_rendering.pack(side="left")
        label_lighting = tk.Label(frame3, text="lighting technology:", anchor=tk.W)
        label_lighting.pack(side="left")

        # FrameRate
        global framerate
        framerate = tk.Entry(frame1)
        framerate.pack(side="right", fill="x", expand=True)
        framerate.bind("<Return>", set_fps)

        # Rendering
        global rendering_mode
        rendering_mode = tk.StringVar(tab)
        rendering = tk.OptionMenu(frame2, rendering_mode, "Direct3D11", "Direct3DFL10", "OpenGL", "Metal", "Vulkan")
        rendering.pack(side="right", fill="x", expand=True)
        rendering_mode.trace("w", set_rendering)

        # Lighting
        global lighting_mode
        lighting_mode = tk.StringVar(tab)
        lighting = tk.OptionMenu(frame3, lighting_mode, "Voxel", "ShadowMap", "Future")
        lighting.pack(side="right", fill="x", expand=True)
        lighting_mode.trace("w", set_lighting)
    if tab_name == "Intergration":
        frame1 = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
        frame2 = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
        frame1.pack(fill="x", pady=5)
        frame2.pack(fill="x", pady=5)

        label_notifcation = tk.Label(frame1, text="Enable notifcations:", anchor=tk.W)
        label_notifcation.pack(side="left")
        label_notifcation_mode = tk.Label(frame2, text="notifcation mode :", anchor=tk.W)
        label_notifcation_mode.pack(side="left")

        # notifcation
        global notification_var
        global notifcation_mode
        notification_var = tk.BooleanVar(tab)
        integration_toggle = tk.Checkbutton(frame1, variable=notification_var, command=toggle_notification)
        integration_toggle.pack(side="right")
        notifcation_mode = tk.StringVar(tab)
        notifcation = tk.OptionMenu(frame2, notifcation_mode, "ServerInfo", "GameInfo")
        notifcation.pack(side="right", fill="x", expand=True)
        notifcation_mode.trace("w", set_notifcation_mode)


window = tk.Tk()
check()
window.title("Bootblox")
window.geometry("400x300")
window.resizable(True, True)
print(check_activity())
window.attributes('-alpha', 0.6)

notebook = ttk.Notebook(window)

create_tab("Intergration", "Things that will improve your experience")
create_tab("FastFlags", "Change the roblox FastFlags")

style = ttk.Style()
style.configure('TNotebook', tabposition='wn')

notebook.pack(fill="both", expand=True)

window.mainloop()
