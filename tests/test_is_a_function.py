from pyds import isAFunction
import unittest


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
            self.assertTrue(isAFunction(item))

        wrongs = [234, "foo", True, False, None, {}, []]

        for item in wrongs:
            self.assertFalse(isAFunction(item))
