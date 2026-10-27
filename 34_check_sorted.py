
def is_sorted(numbers):
    """Return True if the list is sorted in ascending order."""
    return all(
        numbers[i] <= numbers[i + 1]
        for i in range(len(numbers) - 1)
    )