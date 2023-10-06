#!/usr/bin/python3
""" Prime Game Module """


def isPrime(n):
    """
    checks if n is a prime number
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def playRound(n):
    """
    checks how whose turn it is to play
    Maria plays for every odd turns
    Ben plays for every even turns
    """
    turns = 0
    for i in range(1, n + 1):
        if isPrime(i):
            turns += 1

    if turns % 2 == 0:
        return 'Ben'
    else:
        return 'Maria'


def isWinner(x, nums):
    """
    checks the winner by comparing who played most
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if x:
            winner = playRound(n)
            if winner == 'Maria':
                maria_wins += 1
            else:
                ben_wins += 1

            x -= 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
