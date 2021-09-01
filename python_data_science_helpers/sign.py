from .is_a_number import *

def sign(x):
	assert isANumber(x), "`x` must be a number!"

	if x > 0: return 1
	if x < 0: return -1
	return 0
