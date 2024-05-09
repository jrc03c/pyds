from numpy import nan

from .is_a_number import is_a_number


def test():
    numbers = [1, 0, -1, 234.567, -234.567, 1e20, 1e-20]

    for number in numbers:
        assert is_a_number(number)

    others = [
        "234.567",
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: 2 * x,
        [[[234]]],
        [nan],
    ]

    for item in others:
        assert not is_a_number(item)
