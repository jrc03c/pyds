from .is_a_function import is_a_function


def test():
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
        assert is_a_function(item)

    wrongs = [234, "foo", True, False, None, {}, []]

    for item in wrongs:
        assert not (is_a_function(item))
