"""
Definition of the application UI.
"""
import tkinter
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
    frm = ttk.Frame(root, padding=10)
    frm.pack(expand=True, fill="both")
    label = ttk.Label(frm, text="Hello World!")
    label.pack(side="top", padx=5, pady=5)
    button = ttk.Button(frm, text="Quit", command=root.destroy, name="quit")
    button.pack(side="top", padx=5, pady=5)
