import unittest
from pyds import distance


class DistanceTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            distance([3, 4], [0, 0]),
            5,
            msg="Cannot get the distance of a vector from zero!",
        )

        self.assertEqual(
            distance([1, 2, 3], [4, 5, 6]),
            27 ** 0.5,
            msg="Cannot get the distance from one vector to another!",
        )

        self.assertEqual(
            distance(3, 5), 2, msg="Cannot get the distance between two numbers!"
        )

    def testErrors(self):
        a = True
        b = False
        self.assertRaises(AssertionError, distance, a, b)

        a = "foo"
        b = "bar"
        self.assertRaises(AssertionError, distance, a, b)

        a = lambda x: x * 2
        b = lambda x: x * 3
        self.assertRaises(AssertionError, distance, a, b)

        a = {"foo": "bar"}
        b = {"hello": "world"}
        self.assertRaises(AssertionError, distance, a, b)
