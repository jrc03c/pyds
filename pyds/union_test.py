from numpy import array

from .is_equal import is_equal
from .union import union


def test():
    assert is_equal(union([2, 3, 4], [4, 5, 6]), array([2, 3, 4, 5, 6]))
    assert is_equal(union([2, 3, 4], [5, 6, 7]), array([2, 3, 4, 5, 6, 7]))
    assert is_equal(union([2, 3, 4], [4, 3, 2]), array([2, 3, 4]))
    assert is_equal(union([4, 3, 2], [2, 3, 4]), array([4, 3, 2]))


def test_errors():
    pass
