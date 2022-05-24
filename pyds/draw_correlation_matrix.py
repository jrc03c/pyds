from .get_correlation_matrix import getCorrelationMatrix
import matplotlib.pyplot as plot


def drawCorrelationMatrix(a, b):
    temp = getCorrelationMatrix(a, b)
    plot.pcolormesh(temp, vmin=-1, vmax=1)
    plot.show()
    plot.clf()
    return temp
