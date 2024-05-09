from numpy import shape
from numpy.random import normal
from pandas import DataFrame, Series

from .is_equal import is_equal
from .set import set
from .shuffle import shuffle
from .sort import sort


def test():
    a = normal(size=1000)
    b = shuffle(a)
    assert not is_equal(a, b)
    assert is_equal(shape(a), shape(b))
    assert is_equal(sort(set(a)), sort(set(b)))

    a = normal(size=[10, 10, 10, 10])
    b = shuffle(a)
    assert not is_equal(a, b)
    assert is_equal(shape(a), shape(b))
    assert is_equal(sort(set(a)), sort(set(b)))

    a = Series(normal(size=1000))
    b = shuffle(a)
    assert is_equal(sort(set(a)), sort(set(b)))

    a = DataFrame(normal(size=[10, 10]))
    b = shuffle(a)
    assert is_equal(sort(set(a)), sort(set(b)))


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
            shuffle(item)

        except Exception:
            raised = True

        assert raised
