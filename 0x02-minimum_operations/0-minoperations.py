#!/usr/bin/python3
"""Defines minOperations"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file."""
    if n <= 1:
        return 0

    num_operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            num_operations += divisor
        else:
            divisor += 1

    return num_operations
