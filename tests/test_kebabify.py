import unittest

from pyds.kebabify import kebabify


class KebabifyTestCase(unittest.TestCase):
    def test(self):
        rights = [
            ["foobarbaz", "foobarbaz"],
            ["Hello, world! My name is Josh.", "hello-world-my-name-is-josh"],
            [
                "'42 is the number thou shalt count!'",
                "42-is-the-number-thou-shalt-count",
            ],
            ["I don't like you.", "i-dont-like-you"],
            ["how-about-now", "how-about-now"],
        ]

        for pair in rights:
            self.assertEqual(kebabify(pair[0]), pair[1])

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
            self.assertRaises(AssertionError, kebabify, item)
