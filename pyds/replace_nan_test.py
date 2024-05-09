from numpy import nan
from numpy.random import normal

from .is_equal import is_equal
from .replace_nan import replace_nan


def test():
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
        assert is_equal(replace_nan(pair[0]), pair[1])

    assert is_equal(replace_nan([2, 3, "four"], new_value="foobar"), [2, 3, "foobar"])
