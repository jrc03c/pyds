from .is_a_tensor import *
from .is_a_pandas_dataframe import *
from .range import *
from .correl import *
from numpy import mean

def getAverageCorrelation(a, b):
  assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
  assert isATensor(b), "`b` must be a vector, matrix, or tensor!"

  if isAPandasDataFrame(a):
    a = a.values

  if isAPandasDataFrame(b):
    b = b.values

  temp = []

  for i in range(a.shape[1]):
      temp.append(correl(a[:, i], b[:, i]))

  return mean(temp)
