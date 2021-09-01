from numpy import array, ndarray

def isANumpyArray(x):
  t = type(x)
	return t is array or t is ndarray
