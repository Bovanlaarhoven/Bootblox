import tkinter as tk
from tkinter import ttk

def create_tab(tab_name, content):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_name)
    label = tk.Label(tab, text=content)
    label.pack(padx=10, pady=10)

    if tab_name == "Tab 2":
        button = tk.Button(tab, text="Click me!")
        button.pack(pady=10)

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
