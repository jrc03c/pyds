class Foo:
    def bar(self):
        pass


foo = Foo()
eye = lambda x: x
fnTypes = [type(eye), type(foo.bar)]


def isAFunction(x):
    return type(x) in fnTypes

