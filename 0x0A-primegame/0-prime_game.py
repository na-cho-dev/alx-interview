#!/usr/bin/python3
"""
This module contains a function `isWinner`.
"""


def isWinner(x, nums):
    """
    Determines the winner of each game played and returns
    the player with the most wins.

    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player with the most wins, or None if it's a tie
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to limit prime computation
    max_n = max(nums)

    # Sieve of Eratosthenes to precompute prime numbers up to max_n
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Precompute the cumulative count of primes up to each index
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Simulate each game
    for n in nums:
        # The number of prime numbers up to n
        total_primes = prime_counts[n]

        # If total_primes is odd, Maria wins; otherwise, Ben wins
        if total_primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
