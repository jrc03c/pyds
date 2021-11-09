fnType = type(lambda x: x)


def isAFunction(x):
    return type(x) == fnType

