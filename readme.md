# Intro

This package is just a little collection of helper tools and classes for working with `numpy`, `scipy`, `pandas`, and `matplotlib`.

# Installation

Install with `pip`:

```bash
pip install -U git+https://github.com/jrc03c/pyds
```

Or install with `conda`:

```bash
conda install pip git
pip install -U git+https://github.com/jrc03c/pyds
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

Rounds almost-zero values (where `abs(x) < threshold`) to zero. Works on numbers, arbitrarily nested arrays of numbers, numpy arrays, and pandas `DataFrame` and `Series` instances.

---

## `ci_bounds(true, pred, p=95, n=1000, scorer=r_score, progress=lambda x: x)`

Returns the upper and lower confidence interval bounds given two tensors, a percent confidence interval (`p`, which must be between 0 and 100), a number of bootstrap iterations (`n`), a scoring function (`scorer`, which by default is this library's `r_score` function), and a progress callback function (`progress`).

---

## `contains_only_numbers(x)`

Determines whether or not a tensor contains only numbers.

---

## `correl(a, b)`

Computes the correlation between two vectors.

---

## `distance(a, b)`

Computes the Euclidean distance between two tensors of the same shape.

---

## `draw_correlation_matrix(c, neg_hue=0, pos_hue=120)`

Plots a [correlation matrix](#getcorrelationmatrixa-bnone). (This function doesn't actually display the plot yet, though; you'll need to call `matplotlib.pyplot.show()` or similar to display the plot.) The `pos_hue` and `neg_hue` represent hue values as degrees between 0 and 360. See the Seaborn [`diverging_palette`](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html) docs for more info.

---

## `drop_nan(x)`

Drops NaN values from `x`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

---

## `drop_undefined(x, strings=[])`

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

## `find_index(fn, x)`

Returns the index of the first value in `x` that returns `True` when passed into `fn`. This function is similar to JavaScript's [Array.prototype.find_index](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find_index) method _except that_ it returns `None` if no value is found that satisfies the testing function. (JS, on the other hand, returns -1 if no such value is found. Such a strategy wouldn't work in Python because -1 is a valid index into Python arrays.) This function works on arrays of any depth. If `x` is 1-dimensional, then the index returned will be a single whole number. If `x` has 2 or more dimensions, then the index returned will be an array of whole numbers.

For example:

```py
from pyds import find_index

greater_than_six = lambda v: v > 6

x = [2, 3, 4, 5, 6, 7]
find_index(greater_than_six, x)
# 5

y = [[2, 3, 4], [5, 6, 7]]
find_index(greater_than_six, y)
# [1, 2]
# in other words, the value at y[1][2] satisfies the `greater_than_six` function
```

---

## `flatten(x)`

Flattens a tensor to a vector.

---

## `get_average_correlation(a, b)`

Computes the average correlation between pairs of corresponding columns in matrices `a` and `b`.

---

## `get_correlation_matrix(a, b=None)`

Computes the correlation matrix between two matrices by comparing each column in `a` with each column in `b`. If `b` is `None`, then the correlation matrix is computed for `a` against itself.

---

## `Indexer(is_verbose=True)`

This is a class that makes it easy to get rows of data that only exist in certain Series or DataFrames. If `is_verbose` is `True`, the `Indexer` will warn in the console if it fails to remove all missing or NaN values from a transformed data set.

For example, imagine you ran two surveys on the same group of people. In the first survey, most people answered most questions, but a few people either never started the survey or didn't answer all of the questions. The same is true of the second survey, although the people that failed to start or to answer all of the questions in the second survey aren't necessarily the same people as in the first survey. When analyzing the results of the two surveys, we want to line up Person A's responses in the first survey with their responses in the second survey; same for Person B, Person C, and so on. We also want to drop rows that contain missing or NaN values from both data sets. The `Indexer` class is designed to help with those problems.

### Instance methods

#### `.fit(x, y, z, ...)`

Finds and records the intersection of all data set indexes.

#### `.transform(x, y, z, ...)`

Returns subsets of the given data sets using the index from the `fit` method.

Note that the data sets passed into the `fit` method do not have to be the same data sets as the ones passed into the `transform` method.

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

## `is_a_matrix(x)`

Determines whether or not a value is a matrix.

---

## `is_a_number(x)`

Determines whether or not a value is a number.

---

## `is_a_numpy_array(x)`

Determines whether or not a value is a numpy [array](https://numpy.org/doc/stable/reference/generated/numpy.array.html).

---

## `is_a_pandas_dataframe(x)`

Determines whether or not a value is a pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).

---

## `is_a_pandas_series(x)`

Determines whether or not a value is a pandas [Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html).

---

## `is_a_string(x)`

Determines whether or not a value is a string.

---

## `is_a_tensor(x)`

Determines whether or not a value is a tensor.

---

## `is_a_vector(x)`

Determines whether or not a value is a vector.

---

## `is_binary(x)`

Determines whether or not a tensor contains only binary (0 and 1) values.

---

## `is_equal(a, b)`

Determines whether or not two values are equal in a deep sense, though do note that it returns `False` if the two values don't have the same type (e.g., even if a plain Python `list` and a numpy array contain the same numerical values, `is_equal` would return `False` because they aren't the same type; but if you converted them both to the same type, then `is_equal` would return `True` regardless of how "deep" the arrays are).

---

## `is_iterable(x)`

Determines whether or not a value can be iterated over.

---

## `is_jagged(x)`

Determines whether or not a tensor has ragged / jagged edges at any depth.

---

## `is_undefined(x)`

Determines whether or not a value is undefined. A value is considered to be undefined if it's `None`, `math.nan`, or `numpy.nan`.

---

## `least_squares(a, b)`

Solves for `x` in the equation `ax = b` where `a`, `x`, and `b` are all matrices.

---

## `left_pad(x, biggest=None)`

Adds zeros to the left of a number or array of numbers where `biggest` is the maximum possible value. For example, `left_pad(23, 1000)` would return "0023". The `biggest` argument is optional when passing in an tensor of values as `x` since the function will automatically set `biggest` to the largest value in the tensor.

---

## `load_json(path)`

Loads a JSON file from disk.

---

## `magnitude(a)`

Computes the Euclidean norm (i.e., two-norm) of a tensor.

---

## `make_key(n)`

Generates a random alphanumeric string of arbitrary length.

---

## `map(fn, x)`

Returns an array in which `fn` has been applied to each top-level item in the array. Compare with [`apply`](#applyfn-x).

---

## `normalize(x)`

Returns `(x - mean(x)) / std(x)`. Works on arbitrarily nested arrays of numbers, numpy arrays, and pandas `DataFrame` and `Series` instances.

---

## `orthonormalize(x)`

Returns an orthonormalized copy of a matrix in which each column is orthogonal to every other column. The orthonormalization is achieved using the [Gram-Schmidt process](https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process).

---

## `OutlierMitigator(is_allowed_to_clip=True, is_allowed_to_take_the_log=True, max_score=5, should_show_warnings=True)`

This is a class that optionally clips and takes the log of outliers in a vector, matrix, or tensor. The constructor arguments indicate whether or not the mitigator is allowed to clip or take the log of the data if the MAD score of any value exceeds `max_score * MAD`.

The `OutlierMitigator` computes the [MAD](https://en.wikipedia.org/wiki/Median_absolute_deviation) of the data, determines the MAD score of each value (i.e., how many MADs that value is away from the mean), and optionally clips the value to within `max_score` MADs of the mean and/or takes `log(value - min(all_values) + 1)`.

### Instance methods

#### `.fit(x)`

Determines whether or not outliers exist in the given data set and thus whether or not data sets passed into the `transform` function should be modified.

#### `.transform(a, b, c, ...)`

Modifies given data sets if the `fit` method determined that outliers were present in the data set passed into it. If `is_allowed_to_clip == True`, then the data sets are all clipped to the range `[median(x) - max_score * MAD(x), median(x) + max_score * MAD(x)]` (where `x` is the data set that was passed into the `fit` method). If `is_allowed_to_take_the_log == True`, then the natural log of the data set is taken in this way: `log(data - min(x) + 1)`.

Do note that if you pass a data set into `transform` that has a minimum value lower than `min(x)`, a warning will be shown since the mitigator will end up trying to take the log of negative numbers.

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

## `p_value(a, b)`

Returns the _p_-value of two tensors. Obviously, this is an oversimplification, since p-values can be computed in a variety of ways. This function is just short-hand for using scipy's [`ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) function this way:

```python
ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
```

---

## `range(a, b, step=1)`

Returns a range of values.

---

## `reverse(x)`

Reverses a number, string, or array.

---

## `replace_nan(x, new_value=numpy.nan)`

Replaces any NaN values in `x` with the specified new value, which by default is numpy's `nan`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

---

## `replace_undefined(x, new_value=numpy.nan, strings=[])`

Replaces any NaN values in `x` with the specified new value, which by default is numpy's `nan`. Works on pretty much any kind of value, I think. If a vector, matrix, or tensor is passed into the function, then the return value will be a plain Python `list` since the output can potentially be jagged.

By default, values that are considered to be undefined are `None`, `numpy.nan`, and `math.nan`. However, the second parameter gives you the option of passing in a list of strings that are also considered to be undefined. This is useful in cases where you're reading in data from (e.g.) a CSV file that contains empty strings, "NULL", "undefined", etc., and would like to replace those values as well.

---

## `round(x)`

Same as `round_standard(x)`.

---

## `round_standard(x)`

Rounds a number to the nearest integer. Note that this does _not_ have the same functionality as the built-in Python [`round`](https://docs.python.org/3/library/functions.html#round) function _or_ the numpy [`round`](https://numpy.org/doc/stable/reference/generated/numpy.round.html) function! Both of those use "banker's rounding", which rounds numbers that are half-way between two integers (e.g., 2.5) to _the nearest even integer_ (e.g., 1.5 rounds to 2, but 2.5 also rounds to 2)! Instead, this implementation rounds in the "usual" way that we all learned in grade school: numbers exactly half-way between two integers (e.g. 2.5) are always rounded _up_.

Works on numbers, arbitrarily nested arrays of numbers, numpy arrays, and pandas `DataFrame` and `Series` instances.

---

## `r_score(true, pred, baseline=None)`

Computes an R^2 value for two tensors and returns `sign(R^2) * sqrt(abs(R^2))`. If the tensors are binary, R^2 is computed using the _mode_ of `true`; otherwise, it's computed using the _mean_ of `true`. See the `r_squared` function for more information about the `baseline` parameter.

---

## `RScoreManager(should_drop_nan_values=False)`

The `RScoreManager` class is useful for computing aggregate R-scores across cross-validation folds. Technically, you could use this class in cases without cross-validation, but it's overkill there; it'd probably be easier just to use the `r_score` function above. If `should_drop_nan_values` is set to `True`, then `NaN` values will be dropped pair-wise from the `true` and `pred` data sets; and since the `baseline` data set (if used) doesn't need to be paired with anything else, its `NaN` values are just dropped in the usual way.

Internally, the pseudo-code for the R-score calculation is:

```
if is_binaryData(baseline):
  helper = mode
else:
  helper = mean

r_squared = 1 - sum((true - pred) ** 2) / sum((true - helper(baseline)) ** 2)
r_score = sign(r_squared) * sqrt(abs(r_squared))
```

### Instance methods

#### `.update(true, pred, baseline=None)`

Updates the overall score given a single fold's true and predicted values (and optionally a baseline set to compare against). Generally speaking, `baseline` will be the dependent variable's training set, `true` will be the dependent variable's test set, and `pred` will be a model's prediction given the independent variable's test set.

#### `.compute()`

Returns the final R-score. Call this after running through all cross-validation folds.

---

## `r_squared(true, pred, baseline=None)`

Computes an R^2 value for two tensors. If the tensors are binary, R^2 is computed using the _mode_ of `true`; otherwise, it's computed using the _mean_ of `true`.

The formula for R^2 that's used here is:

```
R^2 = 1 - sum((true - pred)**2) / sum((true - mean(true))**2)
```

However, the mean value computed in the denominator can use a different data set, which I've here called `baseline`. By default, `baseline` is the same as `true`. But the `baseline` variable might be useful if computing scores using data that's been split into training and testing sets. For example:

```py
r_squared(y_true_test, y_pred_test, baseline=y_true_train)
```

---

## `save_json(path, x)`

Saves some data to disk as a JSON file. If `x` isn't already a string, then the function will do its best to serialize it and will raise an exception if it's not successful.

---

## `set(x)`

Returns the (flattened) set of values in a tensor.

---

## `shuffle(x)`

Shuffles an array.

---

## `sign(x)`

Gets the sign of a number. For example, `sign(5) == 1`, `sign(-5) == -1`, and `sign(0) == 0`. Works on numbers, arbitrarily nested arrays of numbers, numpy arrays, and pandas `DataFrame` and `Series` instances.

---

## `some(fn, x)`

Returns `True` if some values of `x` return `True` when passed into `fn`; otherwise, returns `False`. This function is similar to JavaScript's [`Array.prototype.some`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some) method.

---

## `sort(x, fn=None)`

Sorts an array, optionally using a function (as in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)) to determine whether items should be moved up or down.

Note that the arguments are reversible to maintain consistency with other similar functions in this library. For example, this works:

```python
sort(lambda a, b: a - b, [3, 2, 4, 3, 5, 4])
```

Unlike most of the other functions in this library, this function does _not_ return a numpy array; it returns a plain ol' Python `list`. I made this choice because the alternative was spending time figuring out types of data in the sorted set, which seemed unnecessarily costly and complex. And if I didn't try to figure out types and just return a numpy array containing the sorted data, it would often complain at me that the array was jagged or that I needed to set `dtype="object"` for the array. So, in the end, it was easiest just to return a `list`.

---

## `truncated_svd(x, rank=1)`

Performs singular value decomposition on a matrix and returns U, Σ, and V matrices that have been truncated to a rank of `rank`.

---

# To do

- Add more tests for the `ci_bounds` function.
- Add tests for the `r_squared` function.
- Make sure that all functions that accept various tensor formats return tensors in those same formats (if possible).
- Make sure that all functions that iterate over arrays (e.g., `find`, `map`, etc.) receive arguments in the same order: function, then array. For example, the signature of `sort` should be `sort(fn, x)` rather than `sort(x, fn)`.

---

# Caveats

I have no idea what I'm doing. I know just enough to be dangerous.
