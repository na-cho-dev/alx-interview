#!/usr/bin/env python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    The function determines if a given data set
    represents a valid UTF-8 encoding.
    """
    bytes_to_process = 0

    for num in data:
        byte = num & 0xFF

        if bytes_to_process == 0:
            if (byte >> 5) == 0b110:
                bytes_to_process = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_process = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_process = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
