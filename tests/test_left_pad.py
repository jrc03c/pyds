import unittest

from numpy import nan

from pyds import leftPad


class LeftPadTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(leftPad(2, 9), "2", msg="Failed to left-pad numbers!")
        self.assertEqual(leftPad(2, 12), "02", msg="Failed to left-pad numbers!")
        self.assertEqual(leftPad(2, 123), "002", msg="Failed to left-pad numbers!")
        self.assertEqual(leftPad(2, 1234), "0002", msg="Failed to left-pad numbers!")

    def testErrors(self):
        wrongs = [
            [234, 123],
            [-234, -234],
            [234.5, 1000],
            [234, 1000.5],
            ["foo", "bar"],
            [True, False],
            [None, None],
            [{"hello": "world"}, {"goodbye": "world"}],
            [lambda x: x * 2, lambda x: x * 3],
            [[1, 10, 100, 1000, nan], 1000],
        ]

        for pair in wrongs:
            self.assertRaises(
                AssertionError,
                leftPad,
                pair[0],
                pair[1],
            )
