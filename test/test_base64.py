"""Tests for the base64 encoding conversions."""
import unittest

from gonverter import base64


class Test(unittest.TestCase):  # pylint: disable=missing-class-docstring
    def test_base64_to_utf8(self) -> None:
        """Test the base64.base64_to_utf8 function."""
        self.assertEqual(base64.base64_to_utf8(""), "")
        self.assertEqual(base64.base64_to_utf8("YQ=="), "a")

    def test_utf8_to_base64(self) -> None:
        """Test the base64.utf8_to_base64 function."""
        self.assertEqual(base64.utf8_to_base64(""), "")
        self.assertEqual(base64.utf8_to_base64("a"), "YQ==")


if __name__ == "__main__":
    unittest.main()
