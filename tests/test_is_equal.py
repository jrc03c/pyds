import unittest
from math import nan as mathNan

from numpy import nan as numpyNan
from numpy.random import normal, seed
from pandas import DataFrame, Series

from pyds import isEqual


class IsEqualTestCase(unittest.TestCase):
    def test(self):
        a = normal(size=100)
        b = normal(size=[100, 100])
        c = normal(size=[100, 100, 100])
        d = Series(normal(size=100))
        e = DataFrame(normal(size=[100, 100]))

        seed(12345)
        f = normal(size=100)
        seed(12345)
        g = normal(size=100)

        class Person:
            def __init__(self, name):
                self.name = name

        person3 = Person("Wilbur")
        person1 = Person("Josh")
        person2 = Person("Josh")
        person1.child = person3
        person2.child = person3

        rights = [
            [234, 234],
            ["foo", "foo"],
            [True, True],
            [False, False],
            [None, None],
            [{"hello": "world"}, {"hello": "world"}],
            [a, a],
            [b, b],
            [c, c],
            [d, d],
            [e, e],
            [f, g],
            [person1, person2],
            [numpyNan, numpyNan],
            [mathNan, mathNan],
            [numpyNan, mathNan],
            [mathNan, numpyNan],
        ]

        for pair in rights:
            self.assertTrue(
                isEqual(pair[0], pair[1]),
                msg="Failed to determine equality! (%s, %s)" % (pair[0], pair[1]),
            )

        wrongs = [
            [234, "234"],
            ["234", True],
            [True, False],
            [False, None],
            [None, {"hello": "world"}],
            [{"hello": "world"}, a],
            [a, b],
            [b, c],
            [c, d],
            [d, e],
            [e, 234],
            [person1, person3],
            [[2, 3, 4], [2, 3, 4, 5]],
        ]

        for pair in wrongs:
            self.assertFalse(
                isEqual(pair[0], pair[1]), msg="Failed to determine inequality!"
            )
