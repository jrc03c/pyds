from numpy import min as oldMin
from .flatten import *


def min(x):
    return oldMin(flatten(x))
