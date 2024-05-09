from numpy import abs, isnan, nan, sqrt

from .r_squared import r_squared
from .sign import sign


def r_score(true, pred, baseline=None):
    r2 = r_squared(true, pred, baseline=baseline)

    if isnan(r2):
        return nan

    return sign(r2) * sqrt(abs(r2))
