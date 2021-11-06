# Intro

This package is just a little collection of helper tools and classes for working with `numpy`, `scipy`, `pandas`, and `matplotlib`.

# Installation

```bash
pip install git+https://github.com/jrc03c/pyds
```

# Usage

```python
from pyds import *
# go on your merry way!
```

# API

## `chop(x, threshold=1e-10)`

rounds almost-zero values (where `abs(x) < threshold`) to zero

---

## `containsOnlyNumbers(x)`

determines whether or not a tensor contains only numbers

---

## `correl(a, b)`

gets the correlation between two vectors

---

## `distance(a, b)`

gets the Euclidean distance between two tensors of the same shape

---

## `drawCorrelationMatrix(a, b)`

plots a [correlation matrix](#get-correlation-matrix)

---

## `filter(fn, arr)`

returns an array containing only items where `fn(item)` is `True`

---

## `flatten(x)`

flattens a tensor to a vector

---

## `getAverageCorrelation(a, b)`

computes the average correlation between two matrices by first computing the [correlation matrix](#get-correlation-matrix) between the two and then averaging all of the values

---

<h2 id="get-correlation-matrix">
  <code>
    getCorrelationMatrix(a, b=None)
  </code>
</h2>

gets the correlation matrix between two matrices by comparing each column in `a` with each column in `b`; if `b` is `None`, then the correlation matrix is computed for `a` against itself

---

## `isAMatrix(x)`

determines whether or not a value is a matrix

---

## `isANumber(x)`

determines whether or not a value is a number

---

## `isANumpyArray(x)`

determines whether or not a value is a numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

---

## `isAPandasDataFrame(x)`

determines whether or not a value is a pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

---

## `isAPandasSeries(x)`

determines whether or not a value is a pandas [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html)

---

## `isAString(x)`

determines whether or not a value is a string

---

## `isATensor(x)`

determines whether or not a value is a tensor

---

## `isAVector(x)`

determines whether or not a value is a vector

---

## `isBinary(x)`

determines whether or not a tensor contains only binary (0 and 1) values

---

## `isEqual(a, b)`

determines whether or not two values are equal in a deep sense, though do note that it returns `False` if the two values don't have the same type (e.g., even if a plain Python `list` and a numpy array contain the same numerical values, `isEqual` would return `False` because they aren't the same type; but if you converted them both to the same type, then `isEqual` would return `True` regardless of how "deep" the arrays are)

---

## `isIterable(x)`

determines whether or not a value can be iterated over

---

## `leastSquares(a, b)`

solves for `x` in the equation `ax = b` where `a`, `x`, and `b` are all matrices

---

## `leftPad(x, biggest=None)`

adds zeros to the left of a number or array of numbers where `biggest` is the maximum possible value; for example, `leftPad(23, 1000)` would return "0023"; `biggest` is optional when passing in an tensor of values as `x` since the function will automatically set `biggest` to the largest value in the tensor

---

## `loadJSON(path)`

loads a JSON file from disk

---

## `magnitude(a)`

gets the two-norm of a tensor

---

## `makeKey(n)`

generates a random alphanumeric string of arbitrary length

---

## `map(fn, arr)`

returns an array in which `fn` has been applied to each item in the array

---

## `pValue(a, b)`

returns the _p_-value of two tensors; obviously, this is an oversimplification, since p-values can be computed in a variety of ways; this function is just short-hand for using scipy's [`ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) function this way:

```python
ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
```

---

## `rScore(true, pred)`

computes an R^2 value for two tensors and returns `sign(R^2) * sqrt(abs(R^2))`; if the tensors are binary, R^2 is computed using the _mode_ of `true`; otherwise, it's computed using the _mean_ of `true`

---

## `range(a, b, step=1)`

returns a range of values

---

## `reverse(x)`

reverses a number, string, or array

---

## `set(x)`

returns the (flattened) set of values in a tensor

---

## `shuffle(x)`

shuffles an array

---

## `sign(x)`

gets the sign of a number; `sign(5) == 1`, `sign(-5) == -1`, and `sign(0) == 0`

---

## `sort(x, fn=None)`

sorts an array, optionally using a function (as in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)) to determine whether items should be moved up or down

---

## `truncatedSVD(x, rank=1)`

performs singular value decomposition on a matrix and returns U, Σ, and V matrices that have been truncated to a rank of `rank`

---

## `Indexer(isVerbose=True)`

This is a class that makes it easy to get rows of data that only exist in certain Series or DataFrames. If `isVerbose` is `True`, the `Indexer` will warn in the console if it fails to remove all missing or NaN values from a transformed data set.

For example, imagine you ran two surveys on the same group of people. In the first survey, most people answered most questions, but a few people either never started the survey or didn't answer all of the questions. The same is true of the second survey, although the people that failed to start or to answer all of the questions in the second survey aren't necessarily the same people as in the first survey. When analyzing the results of the two surveys, we want to line up Person A's responses in the first survey with their responses in the second survey; same for Person B, Person C, and so on. We also want to drop rows that contain missing or NaN values from both data sets. The `Indexer` class is designed to help with those problems.

```python
from pyds import Indexer
from pandas import DataFrame

# Imagine these are the two survey data sets:

survey1 = DataFrame({
  "age": [21, 32, 43, None, 65],
  "name": ["Janet", "Phil", "Rodney", "Alicia", "Marge"],
})

survey2 = DataFrame({
  "color": [None, "red", "green", "blue", "yellow"],
  "name": ["Janet", "Phil", "Rodney", "Alicia", "Marge"],
})

# Notice that Alicia seems to have failed to indicate her
# age in the first survey, and Janet failed to indicate
# a color in the second survey. So, we should probably
# drop Alicia and Janet from the final analysis.

indexer = Indexer()
indexer.mutualFit([survey1, survey2])
survey1 = indexer.transform(survey1)
survey2 = indexer.transform(survey2)

print(survey1)

"""
      age    name
1    32.0    Phil
2    43.0  Rodney
4    65.0   Marge
"""

print(survey2)

"""
    color    name
1     red    Phil
2   green  Rodney
4  yellow   Marge
"""
```

This process works even if the row orders are shuffled! The way it works, though, is by comparing the `index` of each Series or DataFrame, so it's important to make sure that each DataFrame has the correct `index`! It's probably ideal, for example, to assign some unique identifier (like an email address) as the `index` in each data set so that they can be compared correctly.

---

## `OutlierMitigator(canClip=True, canLog=True, mustClip=False, mustLog=False, maxScore=5)`

This is a class that optionally clips and takes the log of outliers in a vector. The constructor arguments indicate whether or not the mitigator _can_ clip or take the log if the MAD score of any value exceeds `maxScore * MAD`, or whether or not the mitigator _must_ clip or take the log regardless of the MAD score of the values.

The `OutlierMitigator` computes the [MAD](https://en.wikipedia.org/wiki/Median_absolute_deviation) of a vector, determines the MAD score of each value (i.e., how many MADs that value is away from the mean), and optionally clips the value to within `maxScore` MADs of the mean and/or takes `log(value - min(allValues) + 1)`.

```python
from pyds import OutlierMitigator

gator = OutlierMitigator()
x = [1, 2, 3, 4, 5, 100]
gator.fit(x)
x = gator.transform(x)

print(x)
# [0. 0.69314718 1.09861229 1.38629436 1.60943791 2.39789527]
```

---

# Caveats

I have no idea what I'm doing. I know just enough to be dangerous.
