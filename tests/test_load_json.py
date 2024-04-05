import os
import shutil
import unittest

from numpy.random import random

from pyds import isEqual, loadJSON, makeKey, saveJSON


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

        saveJSON("temp/" + self.filename, obj)
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
                AssertionError,
                loadJSON,
                item,
            )

        self.assertRaises(
            FileNotFoundError,
            loadJSON,
            makeKey(16),
        )
