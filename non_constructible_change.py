# Given an array of positive integers representing the values of coins in your poosession, write a functio that returns the m8inimum amount of change that you cannot create. coins are positive and not necessarily unique


def nonConstructibleChange(coins):
    # Write your code here.

	coins.sort()

	currentChange = 0
	for coin in coins:
		if coin > currentChange+1:
			return currentChange+1
		currentChange += coin



    return currentChange+1


# Time complexity: O(nlogn) Space complexity:O(1)
