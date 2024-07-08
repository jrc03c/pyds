from numpy import array

from .intersect import intersect
from .is_equal import is_equal


def test():
    assert is_equal(intersect([2, 3, 4], [4, 5, 6]), array([4]))
    assert is_equal(intersect([2, 3, 4], [5, 6, 7]), array([]))
    assert is_equal(intersect([2, 3, 4], [4, 3, 2]), array([2, 3, 4]))
    assert is_equal(intersect([4, 3, 2], [2, 3, 4]), array([4, 3, 2]))


def test_errors():
    pass
