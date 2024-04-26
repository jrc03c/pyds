import unittest

from pyds import is_a_function


class IsAFunctionTestCase(unittest.TestCase):
    def test(self):
        class Foo:
            def bar(self):
                pass

        def eye(x):
            return x

        foo = Foo()

        rights = [
            lambda x: x,
            eye,
            foo.bar,
        ]

        for item in rights:
            self.assertTrue(is_a_function(item))

        wrongs = [234, "foo", True, False, None, {}, []]

        for item in wrongs:
            self.assertFalse(is_a_function(item))
