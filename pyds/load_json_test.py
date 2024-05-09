import os
import shutil

import pytest
from numpy.random import random

from .is_equal import is_equal
from .load_json import load_json
from .make_key import make_key
from .save_json import save_json


@pytest.fixture
def set_up_and_tear_down():
    obj = {}
    temp = obj

    for i in range(0, 100):
        key = make_key(8)

        if random() < 0.25:
            temp[key] = {}
            temp = temp[key]

        else:
            temp[key] = random()

    filename = make_key(8)

    try:
        os.mkdir("temp")
    except Exception:
        pass

    save_json("temp/" + filename, obj)
    obj = obj

    yield {"filename": filename, "obj": obj}

    shutil.rmtree("temp")


def test(set_up_and_tear_down):
    pred = load_json("temp/" + set_up_and_tear_down["filename"])
    assert is_equal(set_up_and_tear_down["obj"], pred)


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
