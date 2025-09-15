#!/usr/bin/python3
def islower(c):
    """
    Checks for a lowercase character.

    Args:
        c: The character to check.

    Returns:
        True if c is lowercase, False otherwise.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
