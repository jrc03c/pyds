from numpy import isnan


def isANumber(x):
    try:
        if isnan(x):
            return False
    except:
        pass

    if type(x) is bool:
        return False

    if type(x) is str:
        return False

    try:
        float(x)
        return True
    except:
        return False
