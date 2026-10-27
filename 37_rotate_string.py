
def rotate_string(text, k):
    """Rotate a string to the right by k positions."""
    if not text:
        return text

    k = k % len(text)

    if k == 0:
        return text

    return text[-k:] + text[:-k]
