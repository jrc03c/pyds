import unittest
from math import nan as mathNaN

from numpy import nan as numpyNaN

from pyds import is_undefined


class IsUndefinedTestCase(unittest.TestCase):
    def test(self):
        undefineds = [None, mathNaN, numpyNaN]

        for value in undefineds:
            self.assertTrue(
                is_undefined(value),
                msg="Incorrectly marked an undefined value as defined!",
            )

        defineds = [234, "foo", True, False, {}, lambda x: x]

        for value in defineds:
            self.assertFalse(
                is_undefined(value),
                msg="Incorrectly marked a defined value as undefined!",
            )
