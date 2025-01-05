"""
Entry point of the application.

Can be called with "python3 -m gonverter".

"""

import logging.config

from gonverter import app

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": [
                "stdout",
            ],
        },
    },
}


def main() -> None:
    """Entry point of the application."""
    application = app.App()
    application.root.mainloop()


if __name__ == "__main__":
    logging.config.dictConfig(logging_config)
    main()
