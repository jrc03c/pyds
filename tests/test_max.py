import unittest
from pyds import max, flatten, reverse
from numpy.random import normal


class MaxTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            max([2, 3, 4]), 4, msg="Failed to get the max value in an array!"
        )

        self.assertEqual(
            max([[[2, 3, 4]]]), 4, msg="Failed to get the max value in an array!"
        )

        x = normal(size=[10, 10, 10, 10])
        yTrue = reverse(sorted(flatten(x)))[0]
        yPred = max(x)
        self.assertEqual(yTrue, yPred, msg="Failed to get the max value in an array!")
