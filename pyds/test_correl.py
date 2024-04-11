from numpy.random import normal, random

from pyds import correl


def test():
    a = random(size=99999)
    b = random(size=99999)

    assert (
        abs(correl(a, a) - 1) < 0.01
    ), "The correlation of two identical vectors should be 1!"

    assert (
        abs(correl(a, -a) + 1) < 0.01
    ), "The correlation of two equal but opposite vectors should be -1!"

    assert (
        abs(correl(a, b)) < 0.01
    ), "The correlation of two random vectors should be close to 0!"

    a = random(size=99999)
    b = a + 1e-5 * normal(size=99999)

    assert (
        abs(correl(a, b)) > 0.99
    ), "The correlation of two almost-identical vectors should be close to 1!"


def test_errors():
    missing = normal(size=1000)
    missing[0] = None

    wrongs = [
        [234, 234],
        [["two", "three", "four"], ["five", "six", "seven"]],
        [normal(size=[50, 50]), normal(size=[50, 50])],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            correl(pair[0], pair[1])
        except Exception:
            raised = True

        assert raised
