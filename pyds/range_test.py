from numpy import array

from .is_equal import is_equal
from .range import range


def test():
    y_true = array([1, 2, 3, 4, 5])
    y_pred = range(1, 6)
    assert is_equal(y_true, y_pred)

    y_true = array([-3.25, -3.5, -3.75, -4.0, -4.25])
    y_pred = range(-3.25, -4.5, -0.25)
    assert is_equal(y_true, y_pred)


def test_errors():
    wrongs = [
        [0, 10, -5],
        [5, -5, 2],
        [0, 10, "two"],
        [0, "ten", 2],
        ["zero", 10, 2],
        [True, False, None],
        [{"hello": "world"}, {"goodbye": "world"}, {"what": "world"}],
        [lambda x: x * 2, lambda x: x * 3, lambda x: x * 4],
    ]

    for trio in wrongs:
        raised = False

        try:
            range(trio[0], trio[1], trio[2])

        except Exception:
            raised = True

        assert raised
