import unittest
from pyds import isAString


class IsAStringTestCase(unittest.TestCase):
    def test(self):
        self.assertTrue(isAString("foo"), msg="Failed to identify a string!")

        others = [
            234,
            True,
            False,
            None,
            ["hello", "world"],
            {"hello": "world"},
            lambda x: x * 2,
        ]

        for item in others:
            self.assertFalse(isAString(item), msg="Failed to identify non-strings!")
