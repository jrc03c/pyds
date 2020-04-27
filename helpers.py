import numpy as np
from scipy.stats import pearsonr
from numpy.linalg import svd, lstsq
from scipy.linalg import diagsvd
import matplotlib.pyplot as plot

def sign(x):
  if x > 0: return 1
  if x < 0: return -1
  return 0

def correl(a, b):
  return pearsonr(a, b)[0]

def customR(true, pred):
  num = np.sum((true - pred)**2)
  den = np.sum((true - np.mean(true))**2)
  if den == 0: return 0
  r2 = 1 - num / den
  return sign(r2) * np.sqrt(np.abs(r2))

def distance(a, b):
  return np.sqrt(np.sum((a - b)**2))

def magnitude(a):
  return distance(a, np.zeros(a.shape))

def leastSquares(a, b):
  return lstsq(a, b, rcond=None)[0]

def getCorrelationMatrix(a, b):
  out = []

  for i in range(0, a.shape[1]):
    row = []

    for j in range(0, b.shape[1]):
      row.append(correl(a[:, i], b[:, j]))

    out.append(row)

  return np.array(out)

def drawCorrelationMatrix(a, b):
  temp = getCorrelationMatrix(a, b)
  plot.pcolormesh(temp, vmin=-1, vmax=1)
  plot.show()
  plot.clf()
  return temp

def getAverageCorrelation(a, b):
  temp = []

  for i in range(a.shape[1]):
      temp.append(correl(a[:, i], b[:, i]))

  return np.mean(temp)

def truncatedSvd(x, rank=1):
  u, s, v = svd(x)
  u = u[:, :rank]
  s = diagsvd(s[:rank], rank, rank)
  v = v[:rank, :]
  return u, s, v
