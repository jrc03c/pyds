# Intro

This package is just a little collection of helper tools and classes for working with `numpy`, `scipy`, `pandas`, and `matplotlib`.

# Installation

Install with `pip`:

```bash
pip install git+https://github.com/jrc03c/pyds
```

Or install with `conda`:

```bash
conda install pip git
pip install git+https://github.com/jrc03c/pyds
```

# Usage

```python
from pyds import *
# go on your merry way!
```

# API

## `apply(fn, x)`

Applies a function to each element in a tensor. Note that this differs from [`map`](#mapfn-arr) in that `map` operates on each top-level item in an array (where each top-level item could itself potentially be an array) whereas `apply` operates on each individual non-array value in an arbitrarily deeply nested and potentially ragged array.

---

## `chop(x, threshold=1e-10)`

Rounds almost-zero values (where `abs(x) < threshold`) to zero.

---

## `containsOnlyNumbers(x)`

Determines whether or not a tensor contains only numbers.

---

## `correl(a, b)`

Gets the correlation between two vectors.

---

## `distance(a, b)`

Gets the Euclidean distance between two tensors of the same shape.

---

## `drawCorrelationMatrix(a, b)`

Plots a [correlation matrix](#getcorrelationmatrixa-bnone).

---

## `dropNaN(x)`

Drops NaN values from `x`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

---

## `dropUndefined(x, strings=[])`

Drops undefined values from `x`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

By default, values that are considered to be undefined are `None`, `numpy.nan`, and `math.nan`. However, the second parameter gives you the option of passing in a list of strings that are also considered to be undefined. This is useful in cases where you're reading in data from (e.g.) a CSV file that contains empty strings, "NULL", "undefined", etc., and would like to drop those values as well.

---

## `every(fn, x)`

Returns `True` if every value of `x` returns `True` when passed into `fn`; otherwise, returns `False`. This function is similar to JavaScript's [`Array.prototype.every`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every) method.

---

## `filter(fn, x)`

Returns an array containing only items where `fn(item)` is `True`.

---

## `find(fn, x)`

Returns the first value in `x` that returns `True` when passed into `fn`. This function is similar to JavaScript's [`Array.prototype.find`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) method. This function works on arrays of any depth.

For example:

```py
from pyds import find

x = [
  [2, 3, 4],
  [5, 6, 7, 8]
]

find(lambda v: v > 5, x)
# 6

find(lambda v: len(v) > 3, x)
# [5, 6, 7, 8]
```

---

## `findIndex(fn, x)`

Returns the index of the first value in `x` that returns `True` when passed into `fn`. This function is similar to JavaScript's [Array.prototype.findIndex](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/findIndex) method _except that_ it returns `None` if no value is found that satisfies the testing function. (JS, on the other hand, returns -1 if no such value is found. Such a strategy wouldn't work in Python because -1 is a valid index into Python arrays.) This function works on arrays of any depth. If `x` is 1-dimensional, then the index returned will be a single whole number. If `x` has 2 or more dimensions, then the index returned will be an array of whole numbers.

For example:

```py
from pyds import findIndex

greaterThanSix = lambda v: v > 6

x = [2, 3, 4, 5, 6, 7]
findIndex(greaterThanSix, x)
# 5

y = [[2, 3, 4], [5, 6, 7]]
findIndex(greaterThanSix, y)
# [1, 2]
# in other words, the value at y[1][2] satisfies the `greaterThanSix` function
```

---

## `flatten(x)`

Flattens a tensor to a vector.

---

## `getAverageCorrelation(a, b)`

Computes the average correlation between two matrices by first computing the [correlation matrix](#getcorrelationmatrixa-bnone) between the two and then averaging all of the values.

---

## `getCorrelationMatrix(a, b=None)`

Gets the correlation matrix between two matrices by comparing each column in `a` with each column in `b`. If `b` is `None`, then the correlation matrix is computed for `a` against itself.

---

## `isAMatrix(x)`

Determines whether or not a value is a matrix.

---

## `isANumber(x)`

Determines whether or not a value is a number.

---

## `isANumpyArray(x)`

Determines whether or not a value is a numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html).

---

## `isAPandasDataFrame(x)`

Determines whether or not a value is a pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

---

## `isAPandasSeries(x)`

Determines whether or not a value is a pandas [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html).

---

## `isAString(x)`

Determines whether or not a value is a string.

---

## `isATensor(x)`

Determines whether or not a value is a tensor.

---

## `isAVector(x)`

Determines whether or not a value is a vector.

---

## `isBinary(x)`

Determines whether or not a tensor contains only binary (0 and 1) values.

---

## `isEqual(a, b)`

Determines whether or not two values are equal in a deep sense, though do note that it returns `False` if the two values don't have the same type (e.g., even if a plain Python `list` and a numpy array contain the same numerical values, `isEqual` would return `False` because they aren't the same type; but if you converted them both to the same type, then `isEqual` would return `True` regardless of how "deep" the arrays are).

---

## `isIterable(x)`

Determines whether or not a value can be iterated over.

---

## `isJagged(x)`

Determines whether or not a tensor has ragged / jagged edges at any depth.

---

## `isUndefined(x)`

Determines whether or not a value is undefined. A value is considered to be undefined if it's `None`, `math.nan`, or `numpy.nan`.

---

## `leastSquares(a, b)`

Solves for `x` in the equation `ax = b` where `a`, `x`, and `b` are all matrices.

---

## `leftPad(x, biggest=None)`

Adds zeros to the left of a number or array of numbers where `biggest` is the maximum possible value. For example, `leftPad(23, 1000)` would return "0023". The `biggest` argument is optional when passing in an tensor of values as `x` since the function will automatically set `biggest` to the largest value in the tensor.

---

## `loadJSON(path)`

Loads a JSON file from disk.

---

## `magnitude(a)`

Gets the two-norm of a tensor.

---

## `makeKey(n)`

Generates a random alphanumeric string of arbitrary length.

---

## `map(fn, x)`

Returns an array in which `fn` has been applied to each top-level item in the array. Compare with [`apply`](#applyfn-x).

---

## `normalize(x)`

Returns `(x - mean(x)) / std(x)`.

---

## `orthonormalize(x)`

Returns an orthonormalized copy of a matrix in which each column is orthogonal to every other column. The orthonormalization is achieved using the [Gram-Schmidt process](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process).

---

## `pValue(a, b)`

Returns the _p_-value of two tensors. Obviously, this is an oversimplification, since p-values can be computed in a variety of ways. This function is just short-hand for using scipy's [`ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) function this way:

```python
ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
```

---

## `replaceNaN(x, newValue=numpy.nan)`

Replaces any NaN values in `x` with the specified new value, which by default is numpy's `nan`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

---

## `replaceUndefined(x, newValue=numpy.nan, strings=[])`

Replaces any NaN values in `x` with the specified new value, which by default is numpy's `nan`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

By default, values that are considered to be undefined are `None`, `numpy.nan`, and `math.nan`. However, the second parameter gives you the option of passing in a list of strings that are also considered to be undefined. This is useful in cases where you're reading in data from (e.g.) a CSV file that contains empty strings, "NULL", "undefined", etc., and would like to replace those values as well.

---

## `rScore(true, pred)`

Computes an R^2 value for two tensors and returns `sign(R^2) * sqrt(abs(R^2))`. If the tensors are binary, R^2 is computed using the _mode_ of `true`; otherwise, it's computed using the _mean_ of `true`.

---

## `RScoreManager(shouldDropNaNValues=False)`

The `RScoreManager` class is useful for computing aggregate R-scores across cross-validation folds. If `shouldDropNaNValues` is set to `True`, then `NaN` values will be dropped pair-wise from the `true` and `pred` data sets; and since the `baseline` data set (if used) doesn't need to be paired with anything else, its `NaN` values are just dropped in the usual way.

Internally, the pseudo-code for the R-score calculation is:

```
if isBinaryData(baseline):
  helper = mode
else:
  helper = mean

rSquared = 1 - sum((true - pred) ** 2) / sum((true - helper(baseline)) ** 2)
rScore = sign(rSquared) * sqrt(abs(rSquared))
```

**Instance methods:**

`.update(true, pred, baseline=None)` = Updates the overall score given a single fold's true and predicted values (and optionally a baseline set to compare against). Generally speaking, `baseline` will be the dependent variable's training set, `true` will be the dependent variable's test set, and `pred` will be a model's prediction given the independent variable's test set.

`.compute()` = Returns the final R-score. Call this after running through all cross-validation folds.

Technically, you could use this class in cases without cross-validation, but it's overkill there; it'd probably be easier just to use the `rScore` function above.

---

## `range(a, b, step=1)`

Returns a range of values.

---

## `reverse(x)`

Reverses a number, string, or array.

---

## `saveJSON(path, x)`

Saves some data to disk as a JSON file. If `x` isn't already a string, then the function will do its best to serialize it and will raise an exception if it's not successful.

---

## `set(x)`

Returns the (flattened) set of values in a tensor.

---

## `shuffle(x)`

Shuffles an array.

---

## `sign(x)`

Gets the sign of a number. For example, `sign(5) == 1`, `sign(-5) == -1`, and `sign(0) == 0`.

---

## `some(fn, x)`

Returns `True` if some values of `x` return `True` when passed into `fn`; otherwise, returns `False`. This function is similar to JavaScript's [`Array.prototype.some`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some) method.

---

## `sort(x, fn=None)`

Sorts an array, optionally using a function (as in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)) to determine whether items should be moved up or down.

Unlike most of the other functions in this library, this function does _not_ return a numpy array; it returns a plain ol' Python `list`. I made this choice because the alternative was spending time figuring out types of data in the sorted set, which seemed unnecessarily costly and complex. And if I didn't try to figure out types and just return a numpy array containing the sorted data, it would often complain at me that the array was jagged or that I needed to set `dtype="object"` for the array. So, in the end, it was easiest just to return a `list`.

---

## `truncatedSVD(x, rank=1)`

Performs singular value decomposition on a matrix and returns U, Σ, and V matrices that have been truncated to a rank of `rank`.

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
indexer.fit(survey1, survey2)
survey1, survey2 = indexer.transform(survey1, survey2)

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

## `OutlierMitigator(isAllowedToClip=True, isAllowedToTakeTheLog=True, maxScore=5, shouldShowWarnings=True)`

This is a class that optionally clips and takes the log of outliers in a vector, matrix, or tensor. The constructor arguments indicate whether or not the mitigator is allowed to clip or take the log of the data if the MAD score of any value exceeds `maxScore * MAD`.

The `OutlierMitigator` computes the [MAD](https://en.wikipedia.org/wiki/Median_absolute_deviation) of the data, determines the MAD score of each value (i.e., how many MADs that value is away from the mean), and optionally clips the value to within `maxScore` MADs of the mean and/or takes `log(value - min(allValues) + 1)`.

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
