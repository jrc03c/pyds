from numpy import max as oldMax
from .flatten import *


def max(x):
    return oldMax(flatten(x))
