from numpy import array, clip, log, median, shape
from numpy.random import normal, random
from pandas import DataFrame, Series

from .is_equal import is_equal
from .make_key import make_key
from .outlier_mitigator import OutlierMitigator
from .r_score import r_score
from .round_standard import round_standard


def test():
    # doesn't do anything to binary data
    x = round_standard(random(size=1000))
    gator = OutlierMitigator()
    y = gator.fit(x).transform(x)
    assert is_equal(x, y)

    # doesn't do anything to data without outliers
    x = random(size=1000)
    gator = OutlierMitigator()
    y = gator.fit(x).transform(x)
    assert is_equal(x, y)

    x = random(size=1000)
    x[-1] = 1e20
    gator = OutlierMitigator()
    y = gator.fit(x).transform(x)
    assert not (is_equal(x, y))

    # neither clip nor log
    x = random(size=1000)
    x[-1] = 1e20
    y_true = x
    gator = OutlierMitigator(is_allowed_to_clip=False, is_allowed_to_take_the_log=False)
    y_pred = gator.fit(x).transform(x)

    assert abs(r_score(y_true, y_pred) - 1) < 0.0001

    # both clip and log
    x = random(size=1000)
    x[-1] = 1e20
    med = median(x)
    mad = median(abs(x - med))
    y_true = clip(x, med - 5 * mad, med + 5 * mad)
    y_true = log(y_true - min(y_true) + 1)
    gator = OutlierMitigator(is_allowed_to_clip=True, is_allowed_to_take_the_log=True)
    y_pred = gator.fit(x).transform(x)

    assert abs(r_score(y_true, y_pred) - 1) < 0.0001

    # both clip and log with custom max score
    x = random(size=1000)
    x[-1] = 1e20
    med = median(x)
    mad = median(abs(x - med))
    max_score = 3
    y_true = clip(x, med - max_score * mad, med + max_score * mad)
    y_true = log(y_true - min(y_true) + 1)

    gator = OutlierMitigator(
        is_allowed_to_clip=True, is_allowed_to_take_the_log=True, max_score=max_score
    )

    y_pred = gator.fit(x).transform(x)

    assert abs(r_score(y_true, y_pred) - 1) < 0.0001

    try:
        gator = OutlierMitigator()
        x = Series(normal(size=1000))
        gator.fit(x).transform(x)
        failed = False

    except Exception:
        failed = True

    assert not failed

    # make sure that multiple data sets can be transformed at once
    train1 = array([1, 2, 3, 4, 1000])
    test1 = array([4, 3, 2, 1])
    gator = OutlierMitigator()
    gator.fit(train1)
    train2, test2 = gator.transform(train1, test1)

    assert not is_equal(train1, train2)
    assert not is_equal(test1, test2)

    # make sure that nothing goes wrong when there's NaNs involved
    x = random(size=1000).tolist()

    for i in range(0, 100):
        funcs = [
            lambda: True,
            lambda: False,
            lambda: None,
            lambda: random(),
            lambda: make_key(8),
        ]

        index = int(random() * len(x))
        func = funcs[int(random() * len(funcs))]
        x[index] = func()

    x = array(x)

    gator = OutlierMitigator()
    nothing_went_wrong = True

    try:
        gator.fit(x).transform(x)

    except Exception:
        nothing_went_wrong = False

    assert nothing_went_wrong

    # make sure that tensors are returned in their original shape
    train = [1, 2, 3, 4, 1000]
    gator = OutlierMitigator(should_show_warnings=False)
    gator.fit(train)

    test1 = normal(size=[2, 3, 4, 5])
    pred1 = gator.transform(test1)
    assert is_equal(shape(test1), shape(pred1))

    test2 = DataFrame(normal(size=[10, 20]))
    pred2 = gator.transform(test2)
    assert is_equal(shape(test2.values), shape(pred2))


def test_errors():
    wrongs = [
        [234, 234],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
    ]

    def helper(a, b):
        gator = OutlierMitigator()
        gator.fit(a).transform(b)

    for pair in wrongs:
        raised = False

        try:
            helper(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
