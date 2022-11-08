import unittest
from pyds import apply, isEqual
from numpy.random import normal

double = lambda x: x * 2


class ApplyTestCase(unittest.TestCase):
    def test(self):
        x = normal(size=[2, 3, 4, 5])

        rights = [
            [apply(double, x), x * 2],
            [apply(x, double), x * 2],
            [
                apply(lambda x: x + "foo", ["a", "b", "c"]).tolist(),
                ["afoo", "bfoo", "cfoo"],
            ],
            [
                apply(double, [[2], [3, 4], [5, 6, 7]]).tolist(),
                [[4], [6, 8], [10, 12, 14]],
            ],
        ]

        for pair in rights:
            self.assertTrue(isEqual(pair[0], pair[1]))

    def testWithLambdaWithoutParams(self):
        x = [2, 3, 4, 5, 6]
        y = apply(lambda: "foo", x)

        for item in y:
            self.assertEqual(item, "foo")

    def testErrors(self):
        wrongs = [
            [double, "foo"],
            [double, True],
            [double, False],
            [double, None],
            [double, {"hello": "world"}],
            [double, double],
            [double, 234],
            ["foo", [2, 3, 4]],
            [True, [2, 3, 4]],
            [False, [2, 3, 4]],
            [None, [2, 3, 4]],
            [{"hello": "world"}, [2, 3, 4]],
            [234, [2, 3, 4]],
            [[2, 3, 4], [2, 3, 4]],
        ]

        for pair in wrongs:
            self.assertRaises(AssertionError, apply, pair[0], pair[1])

