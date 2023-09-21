#!/usr/bin/python3
"""
Change making module.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    count = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
