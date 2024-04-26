from .__helpers__ import alphanumerics, quote_variations


def camelify(text):
    isinstance(text, str), "`text` must be a string!"

    text = text.strip()
    out = ""
    should_capitalize_next_character = False

    for char in text:
        if char.lower() in alphanumerics:
            if len(out) == 0:
                out += char.lower()

            elif should_capitalize_next_character:
                out += char.upper()

            else:
                out += char

            should_capitalize_next_character = False

        elif char not in quote_variations:
            should_capitalize_next_character = True

    return out
