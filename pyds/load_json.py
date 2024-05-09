import json

from .is_a_string import is_a_string


def load_json(path):
    assert is_a_string(path), "`path` must be a string!"

    with open(path) as file:
        return json.load(file)
