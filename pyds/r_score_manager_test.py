import pandas as pd
from numpy import abs, isnan, mean, nan, sqrt, sum
from numpy.random import normal, random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

from .r_score import r_score
from .r_score_manager import RScoreManager
from .sign import sign


def test_perfect_score():
    x = normal(size=1000)
    y = x
    manager = RScoreManager()

    for i in range(0, 10):
        x_temp = x[i * 100 : (i + 1) * 100]
        y_temp = y[i * 100 : (i + 1) * 100]
        manager.update(x_temp, y_temp)

    score = manager.compute()
    assert score == 1


def test_high_score():
    x = normal(size=[1000, 10])
    y = x + 0.01 * normal(size=x.shape)
    x = pd.DataFrame(x)
    y = pd.DataFrame(y)
    manager = RScoreManager()

    for i in range(0, 10):
        x_temp = x.iloc[range(i * 100, (i + 1) * 100), :]
        y_temp = y.iloc[range(i * 100, (i + 1) * 100), :]
        manager.update(x_temp, y_temp)

    score = manager.compute()
    assert score > 0.90


def test_low_score():
    x = normal(size=[10, 20, 30])
    y = normal(size=[10, 20, 30])
    manager = RScoreManager()

    for i in range(0, 10):
        x_temp = x[i]
        y_temp = y[i]
        manager.update(x_temp, y_temp)

    score = manager.compute()
    assert score < 0


def test_baseline():
    x = [1, 2, 3, 4, 5]
    y = [8, 8, 8, 8, 8]
    b = [8]
    manager = RScoreManager()
    manager.update(x, y, baseline=b)
    score = manager.compute()
    assert score == 0


def test_constants():
    true = [6, 6, 6, 6, 6]
    pred = [1, 2, 3, 4, 5]
    manager = RScoreManager()
    manager.update(true, pred)
    score = manager.compute()
    assert isnan(score)


def test_dropping_nan_values():
    x = normal(size=1000)
    y = normal(size=1000)

    for i in range(0, 100):
        index = int(random() * len(x))
        x[index] = None

    for i in range(0, 100):
        index = int(random() * len(y))
        y[index] = nan

    manager = RScoreManager(should_drop_nan_values=True)
    manager.update(x, y)
    score = manager.compute()
    assert not isnan(score)


def test_not_dropping_nan_values():
    x = normal(size=1000)
    y = normal(size=1000)

    for i in range(0, 100):
        index = int(random() * len(x))
        x[index] = None

    for i in range(0, 100):
        index = int(random() * len(y))
        y[index] = nan

    manager = RScoreManager(should_drop_nan_values=False)
    manager.update(x, y)
    score = manager.compute()
    assert isnan(score)


def test_single_fold_against_r_score_function():
    x = normal(size=1000)
    y = x + 0.01 * normal(size=x.shape)
    r1 = r_score(x, y)
    r2 = RScoreManager().update(x, y).compute()
    assert r1 == r2


def test_compare_with_manually_summing():
    x = normal(size=[1000, 3])
    y = normal(size=1000)

    x = pd.DataFrame(x)
    y = pd.DataFrame(y)

    kf = KFold(n_splits=10, shuffle=True)
    manager = RScoreManager()
    sse_test_vs_pred = 0
    sse_test_vs_baseline = 0

    for train_index, test_index in kf.split(x):
        x_train = x.iloc[train_index, :].values
        x_test = x.iloc[test_index, :].values
        y_train = y.iloc[train_index].values
        y_test = y.iloc[test_index].values

        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)

        manager.update(y_test, y_pred, baseline=y_train)
        sse_test_vs_pred += sum((y_test - y_pred) ** 2)
        sse_test_vs_baseline += sum((y_test - mean(y_train)) ** 2)

    score1 = manager.compute()

    r2 = 1 - sse_test_vs_pred / sse_test_vs_baseline
    score2 = sign(r2) * sqrt(abs(r2))

    assert abs(score1 - score2) < 0.01


def test_errors():
    wrongs = [
        [[2, 3, 4], 234],
        [[2, 3, 4], "foo"],
        [[2, 3, 4], True],
        [[2, 3, 4], False],
        [[2, 3, 4], None],
        [[2, 3, 4], nan],
        [[2, 3, 4], {}],
        [[2, 3, 4], lambda x: x],
        [234, [2, 3, 4]],
        ["foo", [2, 3, 4]],
        [True, [2, 3, 4]],
        [False, [2, 3, 4]],
        [None, [2, 3, 4]],
        [nan, [2, 3, 4]],
        [{}, [2, 3, 4]],
        [lambda x: x, [2, 3, 4]],
    ]

    for pair in wrongs:
        manager = RScoreManager()
        raised = False

        try:
            manager.update(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
