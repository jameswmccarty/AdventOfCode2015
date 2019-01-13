#!/usr/bin/python

import math

"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

    The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
    The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
    Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is 33100000.

--- Part Two ---

The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is still 33100000.

"""

def house_presents(house_num):
	factors = set()
	for i in range(1,int(math.ceil(math.sqrt(house_num)))+1):
		if house_num % i == 0:
			factors.add(i)
			factors.add(house_num/i)
	return 10 * sum(factors)	

def house_presents2(house_num):
	factors = set()
	for i in range(1,int(math.ceil(math.sqrt(house_num)))+1):
		if house_num % i == 0:
			factors.add(i)
			factors.add(house_num/i)
	factors = [ x for x in factors if 50*x >= house_num ]
	return 11 * sum(factors)
	
def min_house(goal):
	goal /= 10
	goal *= 2
	n = 1
	while n*(n-1) < goal:
		n+=1
	return n

# invalid approach...
def bin_search(target, L, R):
	while L <= R:
		M = int(math.floor((L+R)/2))
		if house_presents(M) < target:
			L = M + 1
		elif house_presents(M) > target:
			R = M - 1
		else:
			return M
	return M
	
if __name__ == "__main__":

	# Part 1 Solution
	goal = 33100000
	house_num = min_house(goal)
	while house_presents(house_num) < goal:
		house_num += 1
	print house_num
	
	# Part 2 Solution

	house_num = min_house(goal)
	while house_presents2(house_num) < goal:
		house_num += 1
	print house_num