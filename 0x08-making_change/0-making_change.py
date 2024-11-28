#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """

    if (total <= 0):
        return 0

    coins.sort()
    ind = len(coins) - 1
    store = []

    while total > 0 and ind >= 0:
        if total >= coins[ind]:
            store.append(coins[ind])
            total -= coins[ind]
        else:
            ind -= 1

    if total > 0:
        return -1

    return len(store)
