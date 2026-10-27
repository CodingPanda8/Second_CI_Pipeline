
def find_missing_number(numbers):
    """Find the missing number in the range 1 to n."""
    n = len(numbers) + 1
    result = 0

    for number in range(1, n + 1):
        result ^= number

    for number in numbers:
        result ^= number

    return result
