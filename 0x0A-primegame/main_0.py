#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(4, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(-1, [10])))
# nums = [0] * 10000
# for i in range(10000):
#    nums[i] = i

# print("Winner: {}".format(isWinner(10000, nums)))
