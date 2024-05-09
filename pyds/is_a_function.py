class Foo:
    def bar(self):
        pass


fn_types = [type(lambda x: x), type(Foo().bar)]


def is_a_function(x):
    return type(x) in fn_types
