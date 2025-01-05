"""
Runner to run actions inside a tkinter app.
Allow to simulate user interactions for end-to-end testing.
"""
import _tkinter
import logging
import time
import tkinter
import typing
from collections import abc
from unittest import mock

logger = logging.getLogger(__name__)


MAX_TKINTER_UPDATE = 1_000_000
"""
Maximum number of events executed after each actions. Used to prevent infinite loops.
"""


original_mainloop = tkinter.Misc.mainloop
# There are only two way to exit a tkinter app:
# Misc.quit and Tk.destroy, Misc.destroy doesn't exit the app.
original_quit = tkinter.Misc.quit
original_destroy = tkinter.Tk.destroy


Scenario: typing.TypeAlias = abc.Sequence[abc.Callable[[tkinter.Misc], None]]


class ScenarioNotEndedError(Exception):
    """Error raised when the scenario didn't fully run."""


class ApplicationNotClosedError(Exception):
    """Error raised when the scenario didn't close the application.
    The last action of the scenario should be to close the application."""


class ScenarioMissingError(Exception):
    """Error raised when no scenario is defined for a mainloop."""


class Runner:
    """
    Fonctionnalities to run a scenario of actions inside a tkinter application.
    """

    debug_keep_window = False
    """
    Whether to keep the window open or not at the end of the scenario when
    the application wasn't close or when a mainloop is launched without a scenario set."""
    debug_sleep_time = 0
    """
    Time in seconds waited between scenario actions to let the user see
    the effects and the progress of the scenario.
    """
    scenario: Scenario
    step_idx: int
    alive: bool
    """
    We need to track the widget destruction because we keep a reference to
    the root inside our mainloop. As long as we keep the reference to the root,
    it will not be destroyed. So we need to know when we have to remove
    that reference to the root. We remove the reference to the root when our mainloop ends.
    """

    @staticmethod
    def mock_mainloop(root: tkinter.Misc, _: int = 0) -> None:
        """We replace the tkinter mainloop by our version of the mainloop to retrieve
        the root and to play our scenario."""
        Runner.alive = True
        Runner.mainloop(root)

    @staticmethod
    def mock_quit(root: tkinter.Misc) -> None:
        """Mock of tkinter.Misc.quit to break out of our mainloop at application end."""
        Runner.alive = False
        original_quit(root)

    @staticmethod
    def mock_destroy(root: tkinter.Tk) -> None:
        """Mock of tkinter.Tk.destroy to break out of our mainloop at application end."""
        Runner.alive = False
        original_destroy(root)

    @staticmethod
    def mock_show_dialog(**options: typing.Any) -> None:
        """Used to disable tkinter.messagebox with which we can't interact."""
        logger.info(f"skip dialog {options}")

    def __init__(self, scenario: Scenario) -> None:
        cls = self.__class__
        cls.scenario = scenario
        cls.step_idx = 0
        cls.alive = False

    def run(self, launch_app: abc.Callable[[], None]) -> None:
        """Launch the application and check that the scenario ran until completion."""
        if logger.isEnabledFor(logging.DEBUG):
            for i, action in enumerate(self.scenario):
                logger.debug(f"Scenario step {i}: {action.__name__}")
        with (
            mock.patch("tkinter.Misc.mainloop", Runner.mock_mainloop),
            mock.patch("tkinter.Misc.quit", Runner.mock_quit),
            mock.patch("tkinter.Tk.destroy", Runner.mock_destroy),
            mock.patch("tkinter.messagebox._show", Runner.mock_show_dialog),
        ):
            launch_app()
        if self.step_idx != len(self.scenario):
            raise ScenarioNotEndedError(
                f"Scenario did not run fully: {self.step_idx} / {len(self.scenario)}")

    @classmethod
    def mainloop(cls, root: tkinter.Misc) -> None:
        """Our implementation of a tkinter mainloop that run the defined scenario."""
        logger.info(f"Run scenario on {root}")
        while cls.alive and cls.step_idx < len(cls.scenario):
            action = cls.scenario[cls.step_idx]
            logger.debug(f"Run action {cls.step_idx}: {action.__name__}")
            cls.step_idx += 1
            action(root)
            cls.pump_events(root)
            if cls.debug_sleep_time:
                print("-sleep-", end="\r")
                time.sleep(cls.debug_sleep_time)
                print("       ", end="\r")

        logger.info(f"End of scenario on {root}")

        if cls.step_idx > len(cls.scenario):
            # the while loop didn't run  because of no scenario
            if cls.debug_keep_window:
                original_mainloop(root)
            raise ScenarioMissingError(f"The scenario is not defined for the mainloop of '{root}'")

        if cls.alive:
            if cls.debug_keep_window:
                original_mainloop(root)
            raise ApplicationNotClosedError("The scenario ended without closing the application")

    @classmethod
    def pump_events(cls, root: tkinter.Misc) -> None:
        """Update the tkinter application: draw elements, call callbacks, etc.
        like the tkinter mainloop would do."""
        infinite = MAX_TKINTER_UPDATE
        while root.tk.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT) and infinite:
            infinite -= 1  # to prevent infinite loop
