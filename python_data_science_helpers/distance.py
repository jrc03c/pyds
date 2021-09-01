from .is_a_number import *
from .is_a_tensor import *
from numpy import sqrt, sum

def distance(a, b):
	assert isANumber(a) or isATensor(a), "`a` must be a number, vector, matrix, or tensor!"
	assert isANumber(b) or isATensor(b), "`b` must be a number, vector, matrix, or tensor!"
	return sqrt(sum((a - b)**2))
