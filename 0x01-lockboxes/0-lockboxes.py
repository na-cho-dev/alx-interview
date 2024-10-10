#!/usr/bin/python3
"""
This module contains a function that solves the lockboxes task
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes (numbered sequentially from 0 to n - 1)
    can be opened.
    Args:
        boxes - A list of lists.
                A key with the same number as a box opens that box
    Return True if all boxes can be opened, else return False
    """
    # Number of boxes
    n = len(boxes)
    # Create a set to keep track of opened boxes
    opened = set()
    # Add the initially opened box[0]
    opened.add(0)
    # Create a stack to store the boxes that we can open
    keys = [0]

    # Perform depth-first search (DFS) using the stack
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in opened and key < n:
                opened.add(key)
                keys.append(key)

    # Check if all boxes have been opened
    return len(opened) == n
