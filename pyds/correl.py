from scipy.stats import pearsonr

from .contains_only_numbers import contains_only_numbers
from .is_a_vector import is_a_vector


def correl(a, b):
    assert is_a_vector(a), "`a` must be a vector!"
    assert is_a_vector(b), "`b` must be a vector!"
    assert contains_only_numbers(a), "`a` must contain only numbers!"
    assert contains_only_numbers(b), "`b` must contain only numbers!"
    return pearsonr(a, b)[0]
