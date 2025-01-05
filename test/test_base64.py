import unittest

from gonverter import base64


class Test(unittest.TestCase):
    def test_base64_to_utf8(self) -> None:
        self.assertEqual(base64.base64_to_utf8("YQ=="), "a")

    def test_utf8_to_base64(self) -> None:
        self.assertEqual(base64.utf8_to_base64("a"), "YQ==")


if __name__ == "__main__":
    unittest.main()
