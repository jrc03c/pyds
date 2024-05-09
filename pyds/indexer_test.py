from numpy.random import normal, random
from pandas import DataFrame as DF
from pandas import Series

from .contains_only_numbers import contains_only_numbers
from .distance import distance
from .indexer import Indexer
from .is_equal import is_equal
from .range import range


def test():
    s = Series([5, 4, 3, None, 1])
    indexer = Indexer()
    s_prime = indexer.fit(s).transform(s)
    index_true = [0, 1, 2, 4]

    for i in range(0, len(s_prime.index)):
        assert s_prime.index[i] == index_true[i]

    t = Series([None, 20, None, 40, 50])
    indexer.fit(s, t)
    index_true = [1, 4]

    for i in range(0, len(indexer.index)):
        assert indexer.index[i] == index_true[i]

    x = DF(normal(size=[50, 50]))

    for i in range(0, int(0.1 * x.shape[0] * x.shape[1])):
        row = int(random() * x.shape[0])
        col = int(random() * x.shape[1])
        x.values[row][col] = None

    x_prime = indexer.fit(x).transform(x)

    assert contains_only_numbers(x_prime.values)

    # check that the Indexer can fit and transform using multiple data sets
    a = Series([0, 10, 20, None, 40, 50])
    b = Series([None, 1, 2, 3, 4, 5])
    indexer = Indexer()
    indexer.fit(a, b)
    c, d = indexer.transform(a, b)

    assert is_equal(c.index, d.index)
    assert distance(c, [10, 20, 40, 50]) == 0
    assert distance(d, [1, 2, 4, 5]) == 0


def test_errors():
    wrongs = [
        234,
        True,
        "foo",
        {"hello": "world"},
        lambda x: x * 2,
        [2, 3, 4],
        [[[2, 3, 4]]],
    ]

    indexer = Indexer()

    for item in wrongs:
        raised = False

        try:
            indexer.fit(item)

        except Exception:
            raised = True

        assert raised

        # ---

        raised = False

        try:
            indexer.transform(item)

        except Exception:
            raised = True

        assert raised
