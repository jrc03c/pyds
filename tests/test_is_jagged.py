import unittest
from pyds import isJagged


class IsJaggedTestCase(unittest.TestCase):
    def test(self):
        a = [[[2, 3, 4]], [[5, 6, 7]], [[8, 9, 0]]]
        self.assertFalse(isJagged(a))

        b = [[2], [3, 4], [5, 6, 7]]
        self.assertTrue(isJagged(b))

    def testErrors(self):
        pass

