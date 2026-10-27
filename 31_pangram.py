
def is_pangram(text):
    """Check whether a string contains every letter from a to z."""
    letters = set(text.lower())
    return all(letter in letters for letter in "abcdefghijklmnopqrstuvwxyz")
