"""
Entry point of the application.

Can be called with "python3 -m gonverter".

"""

from gonverter import app


def main() -> None:
    """Entry point of the application."""
    application = app.App()
    application.root.mainloop()


if __name__ == "__main__":
    main()
