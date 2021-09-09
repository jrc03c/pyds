from python_data_science_helpers import chop
from numpy.random import *

def test():
  a = random() + 1
  assert chop(a) == a, "Cannot chop a positive number!"

  b = -1 - random()
  assert chop(b) == b, "Cannot chop a negative number!"

  assert chop(0) == 0, "Cannot chop zero!"
  assert chop(1e-20) == 0, "Cannot chop a very small positive number!"
  assert chop(-(1e-20)) == 0, "Cannot chop a very small negative number!"
