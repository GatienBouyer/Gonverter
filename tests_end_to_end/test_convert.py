"""End-to-end test of the 'convert' button."""
import logging
import unittest

from gonverter import __main__
from tkinter_test_util import actions
from tkinter_test_util.runner import Runner

logging.basicConfig(level=logging.INFO)


class Test(unittest.TestCase):  # pylint: disable=missing-class-docstring
    def test_nominal(self) -> None:
        """Nominal use of the application to get the base64 of 'a'."""
        output_text = actions.OutputText()
        runner = Runner([
            *actions.set_input_text("a"),
            *actions.click_convert(),
            *actions.get_output_text(output_text),
            *actions.close_app(),
        ])
        runner.run(__main__.main)
        self.assertEqual(output_text.result, "YQ==\n")


if __name__ == "__main__":
    unittest.main()
