from .is_a_number import *

def leftPad(n, max):
	assert type(n) is int, "`n` must be an integer!"
  assert type(max) is int, "`max` must be an integer!"

	numberOfZeros = len(str(max)) - len(str(n))
	return "0" * numberOfZeros + str(n)
