import unittest
import json
import os
import shutil
from pyds import loadJSON, makeKey
from numpy.random import random


def writeFile(path, data):
    with open(path, "w") as file:
        file.write(data)


def writeJSON(path, obj):
    writeFile(path, json.dumps(obj))


def isEqual(a, b):
    if type(a) != type(b):
        return False

    if type(a) == dict and type(b) == dict:
        aKeys = a.keys()
        bKeys = b.keys()

        if len(aKeys) != len(bKeys):
            return False

        for key in aKeys:
            if key not in bKeys:
                return False

        for key in bKeys:
            if key not in aKeys:
                return False

        for key in aKeys:
            aChild = a[key]
            bChild = b[key]

            if not isEqual(aChild, bChild):
                return False

        return True

    else:
        return a == b


class LoadJSONTestCase(unittest.TestCase):
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

        writeJSON("temp/" + self.filename, obj)
        self.obj = obj

    def tearDown(self):
        shutil.rmtree("temp")

    def test(self):
        pred = loadJSON("temp/" + self.filename)
        self.assertTrue(isEqual(self.obj, pred), msg="Failed to load JSON!")

    def testErrors(self):
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
            self.assertRaises(
                AssertionError, loadJSON, item,
            )

        self.assertRaises(
            FileNotFoundError, loadJSON, makeKey(16),
        )
