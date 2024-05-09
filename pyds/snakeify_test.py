from .snakeify import snakeify


def test():
    rights = [
        ["foobarbaz", "foobarbaz"],
        ["Hello, world! My name is Josh.", "hello_world_my_name_is_josh"],
        [
            "'42 is the number thou shalt count!'",
            "42_is_the_number_thou_shalt_count",
        ],
        ["I don't like you.", "i_dont_like_you"],
        ["how_about_now", "how_about_now"],
    ]

    for pair in rights:
        assert snakeify(pair[0]) == pair[1]


def test_errors():
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
        raised = False

        try:
            snakeify(item)

        except Exception:
            raised = True

        assert raised
