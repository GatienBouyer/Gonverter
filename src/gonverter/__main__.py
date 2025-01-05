"""
Entry point of the application.

Can be called with "python3 -m gonverter".

"""

from gonverter import app


def main() -> None:
    """Entry point of the application."""
    root = app.create_root()
    app.create_ui(root)
    root.mainloop()


if __name__ == "__main__":
    main()
