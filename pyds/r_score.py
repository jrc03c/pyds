from numpy import abs, isnan, nan, sqrt

from .r_squared import rSquared
from .sign import sign


def rScore(true, pred, baseline=None):
    r2 = rSquared(true, pred, baseline=baseline)

    if isnan(r2):
        return nan

    return sign(r2) * sqrt(abs(r2))
