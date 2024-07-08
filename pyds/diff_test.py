from numpy import array

from .diff import diff, diff_both
from .is_equal import is_equal


def test():
    assert is_equal(diff([2, 3, 4], [4, 5, 6]), array([2, 3]))
    assert is_equal(diff([4, 5, 6], [2, 3, 4]), array([5, 6]))
    assert is_equal(diff([234, [567, [890]]], [234, 567]), array([890]))
    assert is_equal(diff([234, 567], [234, [567, [890]]]), array([]))
    assert is_equal(diff_both([2, 3, 4], [4, 5, 6]), array([2, 3, 5, 6]))


def test_errors():
    pass
