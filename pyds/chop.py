from .is_a_number import *
from .is_a_tensor import *
from numpy import abs, array

def chop(x, threshold=1e-10):
  if isANumber(x):
    return 0 if abs(x) < threshold else x

  else:
    assert isATensor(x), "`x` must be a number or a tensor of numbers!"
    return array(list(chop(val, threshold=threshold) for val in x))
