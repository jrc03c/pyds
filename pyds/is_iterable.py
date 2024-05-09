def is_iterable(x):
    try:
        iter(x)
        return True

    except Exception:
        return False
