#!/usr/bin/python3
"""
n a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result in
exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    div_num = 2
    condition = True
    num_of_op = 0

    if n <= 1:
        return 0

    while condition:
        if ((n % div_num == 0) and (n != 1)):
            num_of_op += div_num
            n //= div_num
        elif ((n % div_num != 0) and (n != 1)):
            div_num += 1
        else:
            condition = False

    return num_of_op
