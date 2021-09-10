import unittest
from pyds import filter


class FilterTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(
            filter([1, 2, 3, 4, 5], lambda x: x > 2),
            [3, 4, 5],
            msg="Could not filter a list!",
        )

        self.assertEqual(
            filter([[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]], lambda x: len(x) < 4),
            [[1, 2, 3]],
            msg="Could not filter a tensor!",
        )

    def testErrors(self):
        self.assertRaises(AssertionError, filter, "foo", "bar")

        self.assertRaises(AssertionError, filter, True, False)

        self.assertRaises(AssertionError, filter, 123, 456)

        self.assertRaises(AssertionError, filter, {"foo": "bar"}, {"hello": "world"})

        self.assertRaises(AssertionError, filter, lambda x: x * 2, lambda x: x * 3)

        self.assertRaises(AssertionError, filter, [1, 2, 3], [4, 5, 6])
