from numpy import array, percentile
from numpy.random import random

from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .r_score import rScore


def ciBounds(true, pred, p=95, n=1000, scorer=rScore, progress=lambda x: x):
    if isAPandasDataFrame(true) or isAPandasSeries(true):
        return ciBounds(true.values, pred, p=p, n=n, scorer=scorer, progress=progress)

    if isAPandasDataFrame(pred) or isAPandasSeries(pred):
        return ciBounds(true, pred.values, p=p, n=n, scorer=scorer, progress=progress)

    if type(true) == list:
        true = array(true)

    if type(pred) == list:
        pred = array(pred)

    scores = []

    for i in range(0, n):
        true_temp = []
        pred_temp = []

        while len(true_temp) < true.shape[0]:
            j = int(random() * true.shape[0])
            true_temp.append(true[j])
            pred_temp.append(pred[j])

        score = scorer(true_temp, pred_temp)
        scores.append(score)
        progress(i / (n - 1))

    significance = 100 - p
    lower = percentile(scores, significance / 2)
    upper = percentile(scores, 100 - significance / 2)
    return [lower, upper]
