from numpy.random import normal

from .p_value import p_value


def test():
    a = normal(size=1000)
    b = a + 0.0001 * normal(size=1000)
    assert p_value(a, b) > 0.95

    b += 1000
    assert p_value(a, b) < 0.05


def test_errors():
    missing = normal(size=1000)
    missing[0] = None

    wrongs = [
        [234, 567],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [normal(size=[10, 10]), normal(size=[10, 10])],
        [[1, 2, None], [4, "five", 6]],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            p_value(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
