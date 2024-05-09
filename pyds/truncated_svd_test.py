from numpy import dot, shape, zeros
from numpy.random import normal

from .is_a_vector import is_a_vector
from .r_score import r_score
from .range import range
from .truncated_svd import truncated_svd


def diagonalize(s, size=None):
    assert is_a_vector(s), "`s` must be a vector!"

    if size is None:
        size = len(s)

    out = zeros([size, size])

    for i in range(0, len(s)):
        out[i][i] = s[i]

    return out


def test():
    x = normal(size=[100, 100])
    lastr_score = 1

    u, s, v = truncated_svd(x, shape(x)[1])
    x_prime = dot(dot(u, s), v)

    assert abs(r_score(x, x_prime) - 1) < 0.0001

    for rank in range(100, 1, -5):
        u, s, v = truncated_svd(x, rank)
        x_prime = dot(dot(u, s), v)
        r = r_score(x, x_prime)
        assert r <= lastr_score
        lastr_score = r


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        [234, 567],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [normal(size=1000), 1000],
        [normal(size=[10, 10, 10]), 10],
        missing,
    ]

    for pair in wrongs:
        raised = False

        try:
            truncated_svd(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
