import unittest
from pyds import isJagged
from numpy.random import normal


class IsJaggedTestCase(unittest.TestCase):
    def test(self):
        jag = normal(size=[2, 3, 4, 5]).tolist()
        jag[1][2][3] = jag[1][2][3][:2]

        pairs = [
            [jag, True],
            [[[[2, 3, 4]], [[5, 6, 7]], [[8, 9, 0]]], False],
            [[[2], [3, 4], [5, 6, 7]], True],
            [True, False],
            [False, False],
            [None, False],
            ["foo", False],
            [234, False],
            [{}, False],
            [[], False],
            [lambda x: x, False],
        ]

        for pair in pairs:
            if pair[1] is True:
                self.assertTrue(isJagged(pair[0]))
            else:
                self.assertFalse(isJagged(pair[1]))

    def testErrors(self):
        pass

