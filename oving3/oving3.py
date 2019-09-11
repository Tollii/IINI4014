import math

def is_prime(n):
    """A prime number is only divisible by itself and 1, while composite numbers can be expressed as the product of two integers. Returns true if a given number is a prime number, false otherwise."""

    if n == 1 or n == 0:
        return False

    # If number is 2 it is a prime number, but if it is even and larger than 2, it cannot be a prime number
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    # Need only check the numbers to the product of square root of n times square root of n, as all numbers after it will be the same.
    max_divisor = math.floor(math.sqrt(n))

    # Loops over all odd numbers from 3 until it reaches square root of n, and checks if d divides n evenly
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

for n in range(1000):
    if is_prime(n):
        print("%d is a prime number" % n)
