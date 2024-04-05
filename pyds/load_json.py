import json

from .is_a_string import isAString


def loadJSON(path):
    assert isAString(path), "`path` must be a string!"

    with open(path) as file:
        return json.load(file)
