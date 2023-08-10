#!/usr/bin/python3
"""Defines minOperations"""


def minOperations(n):
    """Performs minOperations on n and
    returns the total number of performed operations to achieve n"""
    clipBoard = ""
    currentString = "H"
    numOfOperation = 0

    while len(currentString) < n:
        if len(currentString) == n:
            break

        if clipBoard == "":
            clipBoard = currentString
            numOfOperation += 1

        if n % len(currentString) == 0 and len(currentString) != 1:
            clipBoard = currentString
            numOfOperation += 1

        currentString += clipBoard
        numOfOperation += 1

    return numOfOperation
