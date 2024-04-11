from .__helpers__ import alphanumerics, quote_variations


def camelify(text):
    isinstance(text, str), "`text` must be a string!"

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

        elif char not in quote_variations:
            shouldCapitalizeNextCharacter = True

    return out
