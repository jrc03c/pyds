from numpy import mean, shape, sqrt, std

from .contains_only_numbers import contains_only_numbers
from .is_a_pandas_series import is_a_pandas_series


def cohens_d(a, b):
    if is_a_pandas_series(a):
        a = a.values

    if is_a_pandas_series(b):
        b = b.values

    shape_a = shape(a)
    shape_b = shape(b)

    assert (
        len(shape_a) == 1
    ), "The `cohens_d` function only works on vectors (i.e., 1-dimensional arrays), but the first value you passed into the function has a shape of ({})!".format(
        (", ").join(shape_a)
    )

    assert (
        len(shape_b) == 1
    ), "The `cohens_d` function only works on vectors (i.e., 1-dimensional arrays), but the second value you passed into the function has a shape of ({})!".format(
        (", ").join(shape_b)
    )

    assert contains_only_numbers(
        a
    ), "The vectors passed into the `cohens_d` function must contain only numbers!"

    assert contains_only_numbers(
        b
    ), "The vectors passed into the `cohens_d` function must contain only numbers!"

    # if the sample sizes are roughly equal, then use this formula:
    len_a = len(a)
    len_b = len(b)
    mean_a = mean(a)
    mean_b = mean(b)
    std_a = std(a)
    std_b = std(b)

    return (mean_a - mean_b) / sqrt(
        ((len_a - 1) * std_a**2 + (len_b - 1) * std_b**2) / (len_a + len_b - 2)
    )
