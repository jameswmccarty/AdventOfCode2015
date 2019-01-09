#!/usr/bin/python

"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""

min_ways = 0

def count_ways(volume, avail):
	if volume == 0:
		return 1
	if volume < 0:
		return 0
	if len(avail) == 0:
		return 0
	for i in range(len(avail)):
		return count_ways(volume-avail[i], avail[i+1:]) + count_ways(volume, avail[i+1:])
		
def count_ways_min(volume, avail, used):
	if volume < 0:
		return float('inf')
	if len(avail) == 0:
		return float('inf')
	if volume == 0:
		return used
	for i in range(len(avail)):
		return min(count_ways_min(volume-avail[i], avail[i+1:], used+1), count_ways_min(volume, avail[i+1:], used))
		
def size_n_ways(volume, avail, limit, used):
	if volume < 0:
		return 0
	if used > limit:
		return 0
	if volume == 0 and used == limit:
		return 1
	if volume == 0 and used != limit:
		return 0
	if len(avail) == 0:
		return 0
	for i in range(len(avail)):
		return size_n_ways(volume-avail[i], avail[i+1:], limit, used+1) + size_n_ways(volume, avail[i+1:], limit, used)
		

if __name__ == "__main__":

	# Part 1 Solution

	bins = []
	
	volume = 150
	
	with open("day17_input", "r") as infile:
		for line in infile.readlines():
			bins.append(int(line.strip()))
	
	print count_ways(volume, bins)
	
	# Part 2 Solution

	print size_n_ways(volume, bins, count_ways_min(volume, bins, 0), 0)

