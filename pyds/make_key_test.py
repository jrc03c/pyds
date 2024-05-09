from numpy.random import random

from .make_key import make_key


def test():
    for i in range(0, 100):
        n = int(random() * 100)

        assert len(make_key(n)) == n


def test_errors():
    wrongs = [
        -234,
        123.456,
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in wrongs:
        raised = False

        try:
            make_key(item)

        except Exception:
            raised = True

        assert raised
