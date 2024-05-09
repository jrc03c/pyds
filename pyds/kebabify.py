from .__helpers__ import clean


def kebabify(text):
    assert isinstance(text, str), "`text` must be a string!"

    words = clean(text).split(" ")

    if len(words) == 0:
        return ""

    if len(words) == 1:
        return words[0]

    return "-".join(words)
