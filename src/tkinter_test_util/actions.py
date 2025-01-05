"""Definition of actions to use inside end-to-end test scenarios."""

import tkinter.ttk
import typing

from tkinter_test_util import runner


class WidgetNotFoundError(Exception):
    """Error raised when no widget correspond to the given name."""


class WidgetWrongTypeError(Exception):
    """Error raised when the widget that correspond to the given name
    is not a subtype of the expected widget class."""


T = typing.TypeVar("T", bound=tkinter.Misc)


def get_widget(root: tkinter.Misc, name: str, widget_type: type[T]) -> T:
    """Return the widget of the given name.
    Check that the type of the widget correspond to the expected one."""
    # inspired by tkinter.Misc.nametowidget
    # but this one search through children too
    if name in root.children:
        widget = root.children[name]
        if not isinstance(widget, widget_type):
            raise WidgetWrongTypeError(f"Widget {name} found but with type {type(widget)}")
        return widget
    for child in root.children.values():
        try:
            cwidget = get_widget(child, name, widget_type)
        except WidgetNotFoundError:
            pass
        else:
            return cwidget
    raise WidgetNotFoundError(f"Fail to find widget {name}")


def close_app() -> runner.Scenario:
    """Return the scenario part to close the application."""
    def close_app_action(root: tkinter.Misc) -> None:
        root.quit()
    return [close_app_action]


def set_input_text(text: str) -> runner.Scenario:
    """Return the scenario part to set the given text inside the text_input."""
    def set_input_text_action(root: tkinter.Misc) -> None:
        text_widget = get_widget(root, "input_text", tkinter.Text)
        text_widget.delete("0.0", "end")
        text_widget.insert("0.0", text)
    return [set_input_text_action]


class OutputText:
    """Object to store the value of the output text box."""
    result: str


def get_output_text(obj: OutputText) -> runner.Scenario:
    """Return the scenario part to get the content of the output text box."""
    def get_output_text_action(root: tkinter.Misc) -> None:
        text_widget = get_widget(root, "output_text", tkinter.Text)
        text = text_widget.get("0.0", "end")
        obj.result = text
    return [get_output_text_action]


def click_convert() -> runner.Scenario:
    """Return the scenario part to click on the convert button."""
    def click_convert_action(root: tkinter.Misc) -> None:
        btn = get_widget(root, "convert_button", tkinter.ttk.Button)
        btn.invoke()
    return [click_convert_action]
