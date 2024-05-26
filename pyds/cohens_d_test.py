from numpy.random import normal

from .cohens_d import cohens_d


def test():
    a = normal(size=10000)
    b = normal(size=10000)
    assert abs(cohens_d(a, a)) == 0
    assert abs(cohens_d(a, b)) < 0.1

    c = normal(size=10000)
    d = normal(size=10000) * 100
    assert abs(cohens_d(c, d)) < 0.1

    e = normal(size=10000)
    f = normal(size=10000) + 110
    assert abs(cohens_d(e, f)) > 100


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
            cohens_d(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
