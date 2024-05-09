from .camelify import camelify


def test():
    rights = [
        ["foobarbaz", "foobarbaz"],
        ["Hello, world! My name is Josh.", "helloWorldMyNameIsJosh"],
        [
            "'42 is the number thou shalt count!'",
            "42IsTheNumberThouShaltCount",
        ],
        ["I don't like you.", "iDontLikeYou"],
        ["how_about_now", "howAboutNow"],
    ]

    for pair in rights:
        assert camelify(pair[0]) == pair[1]


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
            camelify(item)

        except Exception:
            raised = True

        assert raised
