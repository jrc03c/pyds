from .is_a_vector import *
from .is_a_pandas_series import *
from .set import *

def isBinary(x):
	assert isAVector(x), "`x` must be a vector!"
	if isAPandasSeries(x): x = x.values
	s = list(sorted(set(x)))
	return len(s) == 2 and s[0] == 0 and s[1] == 1
