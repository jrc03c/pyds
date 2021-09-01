from .is_a_vector import *
from scipy.stats import pearsonr

def correl(a, b):
	assert isAVector(a), "`a` must be a vector!"
	assert isAVector(b), "`b` must be a vector!"

	return pearsonr(a, b)[0]
