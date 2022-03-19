from numpy import nan
from numpy.random import normal
from pyds import isEqual, replaceNaN
import unittest


class ReplaceNaNTestCase(unittest.TestCase):
    def test(self):
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
                self.friends = []

        alice = Person("Alice", 23)
        bob = Person("Bob", 45)
        cindy = Person("Cindy", 67)
        alice.friends += [bob, cindy]

        x = normal(size=[2, 3, 4, 5])

        rights = [
            [3, 3],
            ["foo", nan],
            [True, nan],
            [False, nan],
            [None, nan],
            [lambda x: x, nan],
            [x, x.tolist()],
            [
                alice,
                {
                    "name": nan,
                    "age": alice.age,
                    "friends": [
                        {"name": nan, "age": bob.age, "friends": []},
                        {"name": nan, "age": cindy.age, "friends": []},
                    ],
                },
            ],
        ]

        for pair in rights:
            self.assertTrue(
                isEqual(replaceNaN(pair[0]), pair[1]),
                msg="Could not correctly replace NaN values in: %s" % pair[0],
            )

        self.assertTrue(
            isEqual(replaceNaN([2, 3, "four"], newValue="foobar"), [2, 3, "foobar"])
        )

