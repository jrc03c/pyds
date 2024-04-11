alphanumerics = "abcdefghijklmnopqrstuvwxyz1234567890"
quote_variations = "'’❜"


def replace_all(text, a, b):
    return b.join(text.split(a))


def clean(text):
    assert isinstance(text, str), "`text` must be a string!"

    double_space = "  "
    single_space = " "
    out = ""

    for char in text:
        char = char.lower()

        if char in alphanumerics:
            out += char

        elif char in quote_variations:
            out += ""

        else:
            out += single_space

    while double_space in out:
        out = replace_all(out, double_space, single_space)

    return out.strip()
