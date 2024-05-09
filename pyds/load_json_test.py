import os
import shutil

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


def test_errors():
    wrongs = [
        234,
        True,
        False,
        None,
        [2, 3, 4],
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in wrongs:
        raised = False

        try:
            load_json(item)

        except Exception:
            raised = True

        assert raised

    raised = False

    try:
        load_json(make_key(16))

    except Exception:
        raised = True

    assert raised
