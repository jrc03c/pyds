import unittest
from pyds import JSObject


class JSObjectTestCase(unittest.TestCase):
    def test(self):
        obj = JSObject({"hello": "world"}, goodbye="world")
        obj.foo = "bar"
        obj.x = 5
        obj.doSomething = lambda thing: "doing: %s" % thing
        obj.child = JSObject()
        obj.child.name = "Bob"

        self.assertEqual(
            obj.hello, "world", msg="Failed to assign a property to a JSObject!"
        )

        self.assertEqual(
            obj.goodbye, "world", msg="Failed to assign a property to a JSObject!"
        )

        self.assertEqual(
            obj.foo, "bar", msg="Failed to assign a property to a JSObject!"
        )

        self.assertEqual(obj.x, 5, msg="Failed to assign a property to a JSObject!")

        self.assertEqual(
            obj.doSomething("whatevs"),
            "doing: whatevs",
            msg="Failed to assign a property to a JSObject!",
        )

        self.assertEqual(
            obj.child.name, "Bob", msg="Failed to assign a property to a JSObject!"
        )

        self.assertEqual(
            obj.doesNotExist, None, msg="Failed to assign a property to a JSObject!"
        )
