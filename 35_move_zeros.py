
def move_zeros(numbers):
    """Move all zeros to the end while preserving element order."""
    non_zeros = [number for number in numbers if number != 0]
    zeros = [number for number in numbers if number == 0]
    return non_zeros + zeros