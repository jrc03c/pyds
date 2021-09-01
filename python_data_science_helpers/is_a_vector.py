from .is_iterable import *
from .is_a_numpy_array import *
from numpy import array

def isAVector(x):
	if not isIterable(x):
    return False

	if not isANumpyArray(x):
		x = array(x)

	return len(x.shape) == 1
