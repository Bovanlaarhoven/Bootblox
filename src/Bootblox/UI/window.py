import sys
import os
import tkinter as tk
from tkinter import ttk

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.input import fps
from Library.input import rendering

def set_fps(event):
    value = framerate.get()
    fps(value)  

def set_rendering(*args):
    value = rendering_mode.get()
    rendering(value)

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
        frame1.pack(fill="x", pady=5)
        frame2.pack(fill="x", pady=5)

        label_input = tk.Label(frame1, text="Framerate limit:", anchor=tk.W)
        label_input.pack(side="left")
        label_rendering = tk.Label(frame2, text="Rendering:", anchor=tk.W)
        label_rendering.pack(side="left")

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


window = tk.Tk()
window.title("Bootblox")
window.geometry("400x300")
window.resizable(True, True)
window.attributes('-alpha', 0.6)

notebook = ttk.Notebook(window)

create_tab("FastFlags", "Change the roblox FastFlags")

style = ttk.Style()
style.configure('TNotebook', tabposition='wn')

notebook.pack(fill="both", expand=True)

window.mainloop()
