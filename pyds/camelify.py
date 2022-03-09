from .__helpers__ import alphanumerics, quoteVariations


def camelify(text):
    assert type(text) == str, "`text` must be a string!"

    text = text.strip()
    out = ""
    shouldCapitalizeNextCharacter = False

    for char in text:
        if char.lower() in alphanumerics:
            if len(out) == 0:
                out += char.lower()

            elif shouldCapitalizeNextCharacter:
                out += char.upper()

            else:
                out += char

            shouldCapitalizeNextCharacter = False

        elif char not in quoteVariations:
            shouldCapitalizeNextCharacter = True

    return out
