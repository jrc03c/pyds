import unittest

from pyds.camelify import camelify


class CamelifyTestCase(unittest.TestCase):
    def test(self):
        rights = [
            ["foobarbaz", "foobarbaz"],
            ["Hello, world! My name is Josh.", "helloWorldMyNameIsJosh"],
            [
                "'42 is the number thou shalt count!'",
                "42IsTheNumberThouShaltCount",
            ],
            ["I don't like you.", "iDontLikeYou"],
            ["howAboutNow", "howAboutNow"],
        ]

        for pair in rights:
            self.assertEqual(camelify(pair[0]), pair[1])

    def testErrors(self):
        wrongs = [
            234,
            True,
            False,
            None,
            [2, 3, 4],
            lambda x: x,
            {"hello": "world"},
        ]

        for item in wrongs:
            self.assertRaises(AssertionError, camelify, item)
