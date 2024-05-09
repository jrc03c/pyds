from .is_a_string import is_a_string


def test():
    assert is_a_string("foo")

    others = [
        234,
        True,
        False,
        None,
        ["hello", "world"],
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in others:
        assert not is_a_string(item)
