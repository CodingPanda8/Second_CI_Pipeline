
def most_frequent(numbers):
    """Return the element that occurs most often."""
    if not numbers:
        return None

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    highest_count = max(counts.values())

    for number in numbers:
        if counts[number] == highest_count:
            return number
