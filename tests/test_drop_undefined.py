from math import nan as mathNaN
from numpy import nan as numpyNaN
from numpy.random import normal
from pandas import DataFrame, Series
from pyds import dropUndefined, isEqual
import unittest


class DropUndefinedTestCase(unittest.TestCase):
    def test(self):
        identity = lambda x: x

        df = DataFrame({"foo": [2, 3, 4], "bar": [5, 6, 7]})
        series = Series(["yes", "no", "maybe so"])
        norm = normal(size=[2, 3, 4, 5])

        x = [
            234,
            mathNaN,
            "foo",
            True,
            False,
            None,
            {"hello": "world"},
            numpyNaN,
            identity,
            [2, None, 3, 4, "NULL", "undefined", ""],
            df,
            series,
            norm,
        ]

        yTrue = [
            234,
            "foo",
            True,
            False,
            {"hello": "world"},
            identity,
            [2, 3, 4],
            df.values.tolist(),
            series.values.tolist(),
            norm.tolist(),
        ]

        strings = [
            "NULL",
            "None",
            "none",
            "Nil",
            "nil",
            "",
            "undefined",
            "Undefined",
            "---",
        ]

        yPred = dropUndefined(x, strings=strings)

        self.assertTrue(
            isEqual(yTrue, yPred),
            msg="Failed to correctly drop undefined values from a list!",
        )

