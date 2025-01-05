"""
Definition of the application UI.
"""
import logging
import tkinter
from tkinter import scrolledtext
from tkinter import ttk

from gonverter import base64

logger = logging.getLogger(__name__)


class App:
    """Main application."""
    root: tkinter.Tk
    text_input: scrolledtext.ScrolledText
    text_output: scrolledtext.ScrolledText

    def __init__(self) -> None:
        self.root = self.create_root()
        self.create_ui()

    @staticmethod
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

    def create_ui(self) -> None:
        """Create the UI inside the root frame of the application."""
        frame = ttk.Frame(self.root, padding=5)
        frame.pack(expand=True, fill="both")
        frame.grid_columnconfigure(index=0, weight=1)
        frame.grid_columnconfigure(index=1, weight=1)
        frame.grid_rowconfigure(index=1, weight=1)
        label_input = ttk.Label(frame, text="Your text", padding=5)
        label_input.grid(column=0, row=0)
        self.text_input = scrolledtext.ScrolledText(frame, name="input_text")
        self.text_input.grid(column=0, row=1, sticky="nswe", padx=5, pady=5)
        label_output = ttk.Label(frame, text="Result", padding=5)
        label_output.grid(column=1, row=0)
        self.text_output = scrolledtext.ScrolledText(frame, state="disabled", name="output_text")
        self.text_output.grid(column=1, row=1, sticky="nswe", padx=5, pady=5)
        convert_button = ttk.Button(frame, text="Convert", padding=5,
                                    command=self.cmd_convert, name="convert_button")
        convert_button.grid(column=0, columnspan=2, row=2)

    def cmd_convert(self) -> None:
        """
        Update the text of the text_output by converting the text from the text_input.
        Command called by the convert button.
        """
        text = self.text_input.get("0.0", "end")
        text = text[:-1]  # remove the last \n character
        logger.info(f"Convert from {'utf-8'} to {'base64'}")
        logger.debug(f"Converting {'utf-8'} text: {text}")
        result = base64.utf8_to_base64(text)
        logger.debug(f"Converted into {'base64'}: {result}")
        self.text_output.configure(state="normal")
        self.text_output.delete("0.0", "end")
        self.text_output.insert("end", result)
        self.text_output.configure(state="disabled")
