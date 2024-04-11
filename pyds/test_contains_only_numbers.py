from numpy import nan
from numpy.random import normal

from pyds import contains_only_numbers


def test():
    assert contains_only_numbers([2, 3, 4])
    assert contains_only_numbers(normal(size=[5, 5, 5, 5]))
    assert not contains_only_numbers(["foo", "bar", "baz"])
    assert not contains_only_numbers([nan, nan, nan])


def test_errors():
    wrongs = [
        234,
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
            contains_only_numbers(item)
        except Exception:
            raised = True

        assert raised
