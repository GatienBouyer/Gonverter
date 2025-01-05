# Gonverter - Tkinter conversion app

## Installation

Create a virtual environment or use an existing one and run the following command:
`pip install -e .`

## Run the application

`python -m gonverter`

## Development

For developers, install the development tools (formatters, linters, etc.):
`pip install -e .[dev]`

### Pre-commit
You can run tools one-by-one or use pre-commit to run them:
- `pip install pre-commit`
- `pre-commit run -a` (where `-a` stand for `--all-files`)
- `pre-commit run -a mypy` (mypy can be replaced by any hook id)
- `pre-commit run` (checks only files that are staged)
- `pre-commit install` (to run all hooks before commiting a change)

### Run tests

There are two type of tests:
- Unit tests: `python -m unittest discover tests`
- End-to-end tests: `python -m unittest discover tests_end_to_end`

Run a singular test file using python: `python path/to/test_feature.py`
