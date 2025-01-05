"""
Definition of the application UI.
"""
import tkinter
from tkinter import scrolledtext
from tkinter import ttk


def create_root() -> tkinter.Tk:
    """Create a new empty root frame for the application."""
    root = tkinter.Tk()
    root.wm_title("Gonverter")
    height = 500
    width = 800
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    return root


def create_ui(root: tkinter.Misc) -> None:
    """Create the UI inside the root frame of the application."""
    frame = ttk.Frame(root, padding=5)
    frame.pack(expand=True, fill="both")
    frame.grid_columnconfigure(index=0, weight=1)
    frame.grid_columnconfigure(index=1, weight=1)
    frame.grid_rowconfigure(index=1, weight=1)
    label_input = ttk.Label(frame, text="Your text", padding=5)
    label_input.grid(column=0, row=0)
    text_input = scrolledtext.ScrolledText(frame)
    text_input.grid(column=0, row=1, sticky="NSWE", padx=5, pady=5)
    label_output = ttk.Label(frame, text="Result", padding=5)
    label_output.grid(column=1, row=0)
    text_output = scrolledtext.ScrolledText(frame, state="disabled")
    text_output.grid(column=1, row=1, sticky="NSWE", padx=5, pady=5)
    convert_button = ttk.Button(frame, text="Convert", padding=5)
    convert_button.grid(column=0, columnspan=2, row=2)
