from numpy import *
from numpy.random import *
from scipy.stats import pearsonr, ttest_ind
from numpy.linalg import svd, lstsq, norm
from scipy.linalg import diagsvd
import matplotlib.pyplot as plot
import pandas as pd

DF = pd.DataFrame
Series = pd.Series

def sign(x):
	assert isANumber(x), "`x` must be a number!"

	if x > 0: return 1
	if x < 0: return -1
	return 0

def correl(a, b):
	assert isAVector(a), "`a` must be a vector!"
	assert isAVector(b), "`b` must be a vector!"

	return pearsonr(a, b)[0]

def rScore(true, pred):
	assert isATensor(true), "`true` must be a vector, matrix, or tensor!"
	assert isATensor(pred), "`pred` must be a vector, matrix, or tensor!"

	if isAPandasDataFrame(true):
		true = true.values

	if isAPandasDataFrame(pred):
		pred = pred.values

	num = sum((true - pred)**2)
	den = sum((true - mean(true))**2)
	if den == 0: return 0
	r2 = 1 - num / den
	return sign(r2) * sqrt(abs(r2))

def distance(a, b):
	assert isANumber(a) or isATensor(a), "`a` must be a number, vector, matrix, or tensor!"
	assert isANumber(b) or isATensor(b), "`b` must be a number, vector, matrix, or tensor!"
	return sqrt(sum((a - b)**2))

def magnitude(a):
	assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
	return norm(a)

def leastSquares(a, b):
	assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
	assert isATensor(b), "`b` must be a vector, matrix, or tensor!"
	return lstsq(a, b, rcond=None)[0]

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

def drawCorrelationMatrix(a, b):
	temp = getCorrelationMatrix(a, b)
	plot.pcolormesh(temp, vmin=-1, vmax=1)
	plot.show()
	plot.clf()
	return temp

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

def truncatedSVD(x, rank=1):
	assert isATensor(x) and not isAVector(x), "`x` must be a matrix or tensor!"
	u, s, v = svd(x)
	u = u[:, :rank]
	s = diagsvd(s[:rank], rank, rank)
	v = v[:rank, :]
	return u, s, v

def leftPad(n, max):
	assert type(n) is int, "`n` must be an integer!"

	numberOfZeros = len(str(max)) - len(str(n))
	return "0" * numberOfZeros + str(n)

def pValue(a, b):
	assert isAVector(a), "`a` must be a vector!"
	assert isAVector(b), "`b` must be a vector!"

	return ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]

def loadJSON(path):
	assert isAString(path), "`path` must be a string!"

	with open(path) as file:
		return json.load(file)

def chop(x, threshold=1e-10):
	if isANumber(x):
		return 0 if abs(x) < threshold else x

	else:
		assert isATensor(x), "`x` must be a number or a tensor of numbers!"
		return array(list(chop(val, threshold=threshold) for val in x))

def isAString(x):
	return type(x) == str

def isIterable(x):
	try:
		iter(x)
		return True
	except:
		return False

def isANumber(x):
	if type(x) is bool:
		return False

	try:
		float(x)
		return True
	except:
		return False

def isAPandasSeries(x):
	return type(x) is pd.Series

def isAPandasDataFrame(x):
	return type(x) is pd.DataFrame

def isANumpyArray(x):
	return type(x) is ndarray

def isAVector(x):
	succeeded = isIterable(x)

	if not isANumpyArray(x):
		x = array(x)

	succeeded = succeeded and len(x.shape) == 1
	return succeeded

def isATensor(x):
	if isIterable(x):
		if isAVector(x):
			return True

		else:
			temp = array(x)

			if len(temp.shape) > 1:
				return True
			else:
				return False

	else:
		return False

def isBinary(x):
	assert isAVector(x), "`x` must be a vector!"
	if isAPandasSeries(x): x = x.values
	s = list(sorted(set(x)))
	return len(s) == 2 and s[0] == 0 and s[1] == 1

class OutlierMitigator():
	def __init__(self, shouldClip=True, shouldLog=True, maxScore=5):
		self.shouldClip = shouldClip
		self.shouldLog = shouldLog
		self.wasClipped = False
		self.wasLogged = False
		self.median = None
		self.mad = None
		self.maxScore = maxScore

	def fit(self, x):
		assert isAVector(x), "`x` must be a vector!"
		if isAPandasSeries(x): x = x.values
		
		wasClipped = False
		wasLogged = False
		mad = None

		if isBinary(x): return

		temp = array(list(sorted(x)))
		m = median(temp)
		mad = median(abs(temp - m))
		
		if mad == 0:
			middle = int(len(temp) / 2)

			before = temp[:middle]
			before = before[where(before < m)[0]]
			before = max(before) if len(before) > 0 else m

			after = temp[middle:]
			after = after[where(after > m)[0]]
			after = min(after) if len(after) > 0 else m

			mad = (after - before) / 2

		if mad == 0:
			score = 0

		else:
			score = max(abs(temp - m) / mad)

		if score > self.maxScore:
			if self.shouldClip:
				wasClipped = True
			
			if self.shouldLog:
				wasLogged = True

		self.wasClipped = wasClipped
		self.wasLogged = wasLogged
		self.median = m
		self.mad = mad

	def transform(self, x):
		assert isAVector(x), "`x` must be a vector!"
		if isAPandasSeries(x): x = x.values

		if self.shouldClip and self.wasClipped:
			x = clip(x, self.median - self.maxScore * self.mad, self.median + self.maxScore * self.mad)
		
		if self.shouldLog and self.wasLogged:
			x = log(x - min(x) + 1)

		return x

class Indexer():
	def __init__(self, isVerbose=True):
		assert type(isVerbose) == bool, "`isVerbose` must be a boolean!"
		self.isVerbose = isVerbose

	def fit(self, x):
		assert isAPandasDataFrame(x) or isAPandasSeries(x), "`x` must be a pandas DataFrame or Series!"
		self.index = x.dropna().index
		return self

	def mutualFit(self, items):
		for item in items:
			assert isAPandasDataFrame(item) or isAPandasSeries(item), "All items must be pandas DataFrames or Series!"

		index = None

		for item in items:
			if index is None:
				index = set(item.dropna().index)
			else:
				index = index.intersection(set(item.dropna().index))

		self.index = list(index)
		return self

	def fitAndTransform(self, x):
		assert isAPandasDataFrame(x) or isAPandasSeries(x), "`x` must be a pandas DataFrame or Series!"
		return self.fit(x).transform(x)

	def transform(self, x):
		assert isAPandasDataFrame(x) or isAPandasSeries(x), "`x` must be a pandas DataFrame or Series!"

		out = x.loc[self.index]

		if self.isVerbose and out.shape[0] != out.dropna().shape[0]:
			print("WARNING: Indexer transformation has not removed all NaN values!")

		return out

# from https://github.com/bcherry/js-py/blob/master/js.py
class JSObject(object):
	def __init__(self, *args, **kwargs):
		for arg in args:
			self.__dict__.update(arg)
		
		self.__dict__.update(kwargs)
	
	def __getitem__(self, name):
		return self.__dict__.get(name, None)
	
	def __setitem__(self, name, val):
		return self.__dict__.__setitem__(name, val)
	
	def __delitem__(self, name):
		if self.__dict__.has_key(name):
			del self.__dict__[name]
	
	def __getattr__(self, name):
		return self.__getitem__(name)
	
	def __setattr__(self, name, val):
		return self.__setitem__(name, val)
	
	def __delattr__(self, name):
		return self.__delitem__(name)
	
	def __iter__(self):
		return self.__dict__.__iter__()
	
	def __repr__(self):
		return self.__dict__.__repr__()
	
	def __str__(self):
		return self.__dict__.__str__()
