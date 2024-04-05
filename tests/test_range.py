import unittest

from numpy import array

from pyds import isEqual, range


class RangeTestCase(unittest.TestCase):
    def test(self):
        yTrue = array([1, 2, 3, 4, 5])
        yPred = range(1, 6)

        self.assertTrue(
            isEqual(yTrue, yPred), msg="Failed to generate the correct range!"
        )

        yTrue = array([-3.25, -3.5, -3.75, -4.0, -4.25])
        yPred = range(-3.25, -4.5, -0.25)

        self.assertTrue(
            isEqual(yTrue, yPred), msg="Failed to generate the correct range!"
        )

    def testErrors(self):
        wrongs = [
            [0, 10, -5],
            [5, -5, 2],
            [0, 10, "two"],
            [0, "ten", 2],
            ["zero", 10, 2],
            [True, False, None],
            [{"hello": "world"}, {"goodbye": "world"}, {"what": "world"}],
            [lambda x: x * 2, lambda x: x * 3, lambda x: x * 4],
        ]

        for trio in wrongs:
            self.assertRaises(AssertionError, range, trio[0], trio[1], trio[2])
