from .is_iterable import *
from .is_a_vector import *
from numpy import array

def isATensor(x):
	if isIterable(x):
		if isAVector(x):
			return True

		else:
			temp = array(x)

			if len(temp.shape) > 1:
				return True
			else:
				return False

	else:
		return False
