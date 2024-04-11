from numpy.random import normal

from .apply import apply
from .is_equal import is_equal


def dubble(x):
    return x * 2


def test():
    x = normal(size=[2, 3, 4, 5])

    rights = [
        [apply(dubble, x), x * 2],
        [apply(x, dubble), x * 2],
        [
            apply(lambda x: x + "foo", ["a", "b", "c"]).tolist(),
            ["afoo", "bfoo", "cfoo"],
        ],
        [
            apply(dubble, [[2], [3, 4], [5, 6, 7]]).tolist(),
            [[4], [6, 8], [10, 12, 14]],
        ],
    ]

    for pair in rights:
        assert is_equal(pair[0], pair[1])


def test_with_lambda_without_params():
    x = [2, 3, 4, 5, 6]
    y = apply(lambda: "foo", x)

    for item in y:
        assert item == "foo"


def test_errors():
    wrongs = [
        [dubble, "foo"],
        [dubble, True],
        [dubble, False],
        [dubble, None],
        [dubble, {"hello": "world"}],
        [dubble, dubble],
        [dubble, 234],
        ["foo", [2, 3, 4]],
        [True, [2, 3, 4]],
        [False, [2, 3, 4]],
        [None, [2, 3, 4]],
        [{"hello": "world"}, [2, 3, 4]],
        [234, [2, 3, 4]],
        [[2, 3, 4], [2, 3, 4]],
    ]

    for pair in wrongs:
        raised = False

        try:
            apply(pair[0], pair[1])
        except Exception:
            raised = True

        assert raised
