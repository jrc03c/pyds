import unittest
from pyds import isANumber


class IsANumberTestCase(unittest.TestCase):
    def test(self):
        numbers = [1, 0, -1, 234.567, -234.567, 1e20, 1e-20]

        for number in numbers:
            self.assertTrue(isANumber(number), msg="Fails to identify numbers!")

        others = [
            "234.567",
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            lambda x: 2 * x,
            [[[234]]],
        ]

        for item in others:
            self.assertFalse(isANumber(item), msg="Fails to identify non-numbers!")
