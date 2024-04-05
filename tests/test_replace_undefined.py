import unittest

from numpy import nan
from numpy.random import normal

from pyds import isEqual, replaceUndefined


class ReplaceUndefinedTestCase(unittest.TestCase):
    def test(self):
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
                self.friends = []
                self.empty1 = nan
                self.empty2 = None

        alice = Person("Alice", 23)
        bob = Person("Bob", 45)
        cindy = Person("Cindy", 67)
        alice.friends += [bob, cindy]

        x = normal(size=[2, 3, 4, 5])
        identity = lambda x: x

        rights = [
            [3, 3],
            ["foo", "foo"],
            [True, True],
            [False, False],
            [None, nan],
            [identity, identity],
            [x, x.tolist()],
            [
                alice,
                {
                    "name": alice.name,
                    "age": alice.age,
                    "empty1": nan,
                    "empty2": nan,
                    "friends": [
                        {
                            "name": bob.name,
                            "age": bob.age,
                            "friends": [],
                            "empty1": nan,
                            "empty2": nan,
                        },
                        {
                            "name": cindy.name,
                            "age": cindy.age,
                            "friends": [],
                            "empty1": nan,
                            "empty2": nan,
                        },
                    ],
                },
            ],
        ]

        for pair in rights:
            self.assertTrue(
                isEqual(replaceUndefined(pair[0]), pair[1]),
                msg="Could not correctly replace NaN values in: %s" % pair[0],
            )

        self.assertTrue(
            isEqual(
                replaceUndefined(
                    [2, 3, None, "hahaha"], newValue="foobar", strings=["hahaha"]
                ),
                [2, 3, "foobar", "foobar"],
            )
        )
