from math import nan

from numpy.random import normal, random
from pandas import DataFrame, Series

from .apply import apply
from .is_equal import is_equal
from .round_standard import round_standard
from .sign import sign


def test():
    a = DataFrame([[0.1] * 10] * 10)
    b_true = DataFrame([[0] * 10] * 10)
    b_pred = round_standard(a)
    assert is_equal(b_true, b_pred)

    c = DataFrame([[0.9] * 10] * 10)
    d_true = DataFrame([[1] * 10] * 10)
    d_pred = round_standard(c)
    assert is_equal(d_true, d_pred)

    e = normal(size=[10, 10]).tolist()
    f_true = []

    for i in range(0, len(e)):
        row = e[i]
        temp = []

        for j in range(0, len(row)):
            value = row[j]

            if abs(value) - int(abs(value)) < 0.5:
                temp.append(int(value))

            else:
                temp.append(int(value) + sign(value))

        f_true.append(temp)

    f_pred = round_standard(e)
    print(DataFrame(f_true), "\n")
    print(DataFrame(f_pred))
    assert is_equal(f_true, f_pred)

    assert round_standard(-0.5) == -1
    assert round_standard(-1.5) == -2
    assert round_standard(-3.1) == -3
    assert round_standard(-3.9) == -4

    g = Series(random(size=100))
    h_true = Series([int(v) if v - int(v) < 0.5 else int(v) + 1 for v in g.tolist()])
    h_pred = round_standard(g)
    assert is_equal(h_true, h_pred)

    i = normal(size=[2, 3, 4, 5, 6]).tolist()

    j_true = apply(
        lambda v: int(v) if abs(v) - int(abs(v)) < 0.5 else int(v) + sign(v), i
    ).tolist()

    j_pred = round_standard(i)
    assert is_equal(j_true, j_pred)

    k = ["hello", 234, "world", 567.890]
    l_true = [nan, 234, nan, 568]
    l_pred = round_standard(k)
    assert is_equal(l_true, l_pred)
