alphanumerics = "abcdefghijklmnopqrstuvwxyz1234567890"
quoteVariations = "'’❜"


def replaceAll(text, a, b):
    return b.join(text.split(a))


def clean(text):
    assert type(text) == str, "`text` must be a string!"

    doubleSpace = "  "
    singleSpace = " "
    out = ""

    for char in text:
        char = char.lower()

        if char in alphanumerics:
            out += char

        elif char in quoteVariations:
            out += ""

        else:
            out += singleSpace

    while doubleSpace in out:
        out = replaceAll(out, doubleSpace, singleSpace)

    return out.strip()
