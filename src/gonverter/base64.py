"""
Conversion functions from and to the base64 encoding.
"""

import base64


def base64_to_utf8(text: str) -> str:
    """Translate a string encoded in base64 into utf8."""
    return base64.b64decode(text.encode()).decode()


def utf8_to_base64(text: str) -> str:
    """Translate a string encoded in utf8 into base64."""
    return base64.b64encode(text.encode()).decode()
