import sys
import os
import tkinter as tk
from tkinter import ttk

library_parent_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.append(library_parent_dir)

from Library.input import fps

def set_fps(event):
    value = entry.get()
    fps(value)  

def create_tab(tab_name, content):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)

    label_frame = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
    label_frame.pack(fill="x", pady=1)

    label = tk.Label(label_frame, text=content, anchor=tk.W)
    label.pack(fill="x")

    if tab_name == "FastFlags":
        label_input_frame = tk.Frame(tab, borderwidth=1, relief="solid", padx=5, pady=5)
        label_input_frame.pack(fill="x", pady=5)

        label_input = tk.Label(label_input_frame, text="Framerate limit:", anchor=tk.W)
        label_input.pack(side="left")

        global entry
        entry = tk.Entry(label_input_frame)
        entry.pack(side="right", fill="x", expand=True)

        entry.bind("<Return>", set_fps)

window = tk.Tk()
window.title("Bootblox")
window.geometry("400x300")
window.resizable(True, True)
window.attributes('-alpha', 0.6)

notebook = ttk.Notebook(window)

create_tab("FastFlags", "Change the roblox FastFlags")
create_tab("Tab 2", "Content for Tab 2 goes here")
create_tab("Tab 3", "Different content for Tab 3")

style = ttk.Style()
style.configure('TNotebook', tabposition='wn')

notebook.pack(fill="both", expand=True)

window.mainloop()
