from .is_a_tensor import *
from .is_a_pandas_dataframe import *
from .range import *
from numpy import array

def getCorrelationMatrix(a, b):
  assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
  assert isATensor(b), "`b` must be a vector, matrix, or tensor!"

  if isAPandasDataFrame(a):
    a = a.values

  if isAPandasDataFrame(b):
    b = b.values

  out = []

  for i in range(0, a.shape[1]):
    row = []

    for j in range(0, b.shape[1]):
      row.append(correl(a[:, i], b[:, j]))

    out.append(row)

  return array(out)
