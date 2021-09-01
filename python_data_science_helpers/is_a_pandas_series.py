import pandas as pd

def isAPandasSeries(x):
	return type(x) is pd.Series
