from numpy.random import normal
from pyds import dropNaN, isEqual
import unittest


class DropNaNTestCase(unittest.TestCase):
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
            ["foo", None],
            [True, None],
            [False, None],
            [None, None],
            [lambda x: x, None],
            [x, x.tolist()],
            [
                alice,
                {
                    "age": alice.age,
                    "friends": [
                        {"age": bob.age, "friends": []},
                        {"age": cindy.age, "friends": []},
                    ],
                },
            ],
        ]

        for pair in rights:
            self.assertTrue(
                isEqual(dropNaN(pair[0]), pair[1]),
                msg="Could not correctly drop NaN values from: %s" % pair[0],
            )
