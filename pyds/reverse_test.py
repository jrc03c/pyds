from numpy import array
from numpy.random import normal

from .is_equal import is_equal
from .reverse import reverse


def test():
    x = [1, 3, 5, 6, 4, 2]
    y_true = array([2, 4, 6, 5, 3, 1])
    y_pred = reverse(x)

    assert is_equal(y_true, y_pred)

    a = normal(size=[10, 10, 10, 10])
    b = reverse(a)

    for i in range(0, len(a)):
        assert is_equal(a[i], b[-i - 1])

    assert reverse(234) == 432
    assert reverse("abc") == "cba"


def test_errors():
    wrongs = [
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in wrongs:
        raised = False

        try:
            reverse(item)

        except Exception:
            raised = True

        assert raised
