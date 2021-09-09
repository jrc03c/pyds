import numpy

def shuffle(arr):
  out = numpy.copy(arr)
  numpy.random.shuffle(out)
  return list(out)
