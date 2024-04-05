import os
import shutil
import unittest

import pandas as pd
from numpy.random import random

from pyds import isEqual, loadJSON, makeKey, saveJSON


class SaveJSONTestCase(unittest.TestCase):
    def setUp(self):
        obj = {}
        temp = obj

        for i in range(0, 100):
            key = makeKey(8)

            if random() < 0.25:
                temp[key] = {}
                temp = temp[key]
            else:
                temp[key] = random()

        self.filename = makeKey(8)

        try:
            os.mkdir("temp")
        except:
            pass

        saveJSON("temp/" + self.filename, obj)
        self.obj = obj

    def tearDown(self):
        shutil.rmtree("temp")

    def test(self):
        pred = loadJSON("temp/" + self.filename)
        self.assertTrue(isEqual(self.obj, pred), msg="Failed to load JSON!")

        # test cyclic objects
        x = {}
        x["me"] = x
        failed = False

        try:
            saveJSON("temp/" + makeKey(8), x)

        except:
            failed = True

        self.assertFalse(failed, "Failed to serialize a cyclic object!")

        # test numpy arrays
        x = random(size=[100])
        failed = False

        try:
            saveJSON("temp/" + makeKey(8), x)

        except:
            failed = True

        self.assertFalse(failed, "Failed to save a numpy array as a JSON file!")

        # test pandas series
        x = pd.Series(random(size=[100]))
        failed = False

        try:
            saveJSON("temp/" + makeKey(8), x)

        except:
            failed = True

        self.assertFalse(failed, "Failed to save a pandas Series as a JSON file!")

        # test pandas dataframes
        x = pd.DataFrame(random(size=[10, 10]))
        failed = False

        try:
            saveJSON("temp/" + makeKey(8), x)

        except:
            failed = True

        self.assertFalse(failed, "Failed to save a pandas DataFrame as a JSON file!")

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
            path = "temp/{}.json".format(makeKey(8))
            saveJSON(path, true)
            pred = loadJSON(path)
            self.assertTrue(isEqual(true, pred))
            os.remove(path)

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        path = "temp/{}.json".format(makeKey(8))
        alice = Person("Alice", 23)
        saveJSON(path, alice)
        aliceTrue = {"age": 23, "name": "Alice"}
        alicePred = loadJSON(path)
        self.assertTrue(type(aliceTrue) == type(alicePred))
        self.assertTrue(isEqual(list(alicePred.keys()), list(aliceTrue.keys())))

        for key in alicePred.keys():
            self.assertTrue(isEqual(alicePred[key], aliceTrue[key]))
