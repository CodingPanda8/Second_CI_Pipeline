
def first_non_repeating(text):
    """Return the first character that occurs only once."""
    for char in text:
        if text.count(char) == 1:
            return char
    return None
