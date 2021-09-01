from .is_a_vector import *
from scipy.stats import ttest_ind

def pValue(a, b):
	assert isAVector(a), "`a` must be a vector!"
	assert isAVector(b), "`b` must be a vector!"

	return ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
