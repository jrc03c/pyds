from numpy.random import normal

from .is_equal import is_equal
from .sort import sort


def test():
    x = [5, 3, 1, 2, 4, 6]
    y_true = [1, 2, 3, 4, 5, 6]
    y_pred = sort(x)
    assert is_equal(y_true, y_pred)

    x = normal(size=1000)
    y_true = list(sorted(x.tolist()))
    y_pred = sort(x)
    assert is_equal(y_true, y_pred)

    x = [{"name": "Alice"}, {"name": "Charlie"}, {"name": "Bob"}]
    y_true = [{"name": "Charlie"}, {"name": "Bob"}, {"name": "Alice"}]
    y_pred1 = sort(x, lambda a, b: 1 if a["name"] < b["name"] else -1)
    y_pred2 = sort(lambda a, b: 1 if a["name"] < b["name"] else -1, x)
    assert is_equal(y_true, y_pred1)
    assert is_equal(y_true, y_pred2)


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
            sort(item)

        except Exception:
            raised = True

        assert raised
