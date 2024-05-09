from numpy.random import normal

from .ci_bounds import ci_bounds
from .r_score import r_score


def test():
    a = normal(size=100)
    b = a + 0.25 * normal(size=a.shape[0])
    r = r_score(a, b)
    ci = ci_bounds(a, b)
    assert ci[0] < r
    assert ci[1] > r
    assert r - 0.5 < ci[0]
    assert r + 0.5 > ci[1]
