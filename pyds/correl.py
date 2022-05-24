from .contains_only_numbers import containsOnlyNumbers
from .is_a_vector import isAVector
from scipy.stats import pearsonr


def correl(a, b):
    assert isAVector(a), "`a` must be a vector!"
    assert isAVector(b), "`b` must be a vector!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"
    return pearsonr(a, b)[0]
