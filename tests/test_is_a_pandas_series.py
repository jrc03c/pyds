import unittest

from numpy.random import normal
from pandas import DataFrame, Series

from pyds import isAPandasSeries


class IsAPandasSeriesTestCase(unittest.TestCase):
    def test(self):
        series = [Series(dtype="object"), Series(normal(size=100))]

        for s in series:
            self.assertTrue(isAPandasSeries(s), msg="Failed to identify pandas Series!")

        others = [
            234,
            "foo",
            True,
            False,
            None,
            {"hello", "world"},
            lambda x: x * 2,
            [2, 3, 4, 5],
            DataFrame(normal(size=[100, 100])),
        ]

        for item in others:
            self.assertFalse(
                isAPandasSeries(item), msg="Failed to identify non-pandas-Series!"
            )
