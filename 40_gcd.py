
def gcd(a, b):
    """Find the greatest common divisor using Euclid's algorithm."""
    a, b = abs(a), abs(b)

    while b:
        a, b = b, a % b

    return a
