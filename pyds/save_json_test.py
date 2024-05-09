import os
import shutil

import pandas as pd
from numpy.random import random

from .is_equal import is_equal
from .load_json import load_json
from .make_key import make_key
from .save_json import save_json


# note: figure out how to turn the `setUp` and `tearDown` functions into py_test fixtures!
def setUp(self):
    obj = {}
    temp = obj

    for i in range(0, 100):
        key = make_key(8)

        if random() < 0.25:
            temp[key] = {}
            temp = temp[key]

        else:
            temp[key] = random()

    self.filename = make_key(8)

    try:
        os.mkdir("temp")
    except Exception:
        pass

    save_json("temp/" + self.filename, obj)
    self.obj = obj


def tearDown(self):
    shutil.rmtree("temp")


def test():
    pred = load_json("temp/" + self.filename)
    assert is_equal(self.obj, pred)

    # test cyclic objects
    x = {}
    x["me"] = x
    failed = False

    try:
        save_json("temp/" + make_key(8), x)

    except Exception:
        failed = True

    assert not failed

    # test numpy arrays
    x = random(size=[100])
    failed = False

    try:
        save_json("temp/" + make_key(8), x)

    except Exception:
        failed = True

    assert not failed

    # test pandas series
    x = pd.Series(random(size=[100]))
    failed = False

    try:
        save_json("temp/" + make_key(8), x)

    except Exception:
        failed = True

    assert not failed

    # test pandas dataframes
    x = pd.DataFrame(random(size=[10, 10]))
    failed = False

    try:
        save_json("temp/" + make_key(8), x)

    except Exception:
        failed = True

    assert not failed

    # test lots of data types
    values = [
        234,
        "foo",
        True,
        False,
        None,
        [2, 3, "four", [5, 6, {"seven": 8}]],
        {"hello": "world"},
    ]

    for true in values:
        path = "temp/{}.json".format(make_key(8))
        save_json(path, true)
        pred = load_json(path)
        assert is_equal(true, pred)
        os.remove(path)

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    path = "temp/{}.json".format(make_key(8))
    alice = Person("Alice", 23)
    save_json(path, alice)
    alice_true = {"age": 23, "name": "Alice"}
    alice_pred = load_json(path)
    assert isinstance(alice_true, type(alice_pred))
    assert is_equal(list(alice_pred.keys()), list(alice_true.keys()))

    for key in alice_pred.keys():
        assert is_equal(alice_pred[key], alice_true[key])
