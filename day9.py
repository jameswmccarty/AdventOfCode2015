#!/usr/bin/python

import itertools

"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

"""

def dp_tsp(cities, costs, opt):
	if opt == max:
		base = 0
	elif opt == min:
		base = float('inf')
	else:
		base = 0		
	best_path = base	
	# base cases
	for idx in range(len(cities)):
		# minimal path sets
		# ( 'start', {visited, nodes} ) : cost
		g = dict()
		for j in range(len(cities)): # direct path
			if j != idx:
				g[(cities[j], frozenset())] = 0 # costs[(cities[j], cities[idx])]
		for k in range(1,len(cities)): # k is set size
			for i in range(len(cities)):
				visit_list = itertools.combinations([x for x in cities if x != cities[i] and x != cities[idx]], k)
				for subset in visit_list:
					best = base
					for elem in subset:
						best = opt(best, costs[(cities[i], elem)] + g[(elem, frozenset(set(subset).difference({elem})))])
					g[(cities[i], frozenset(subset))] = best
		# find optimal tour
		best = base
		subset = frozenset(set(cities).difference({cities[idx]}))
		for elem in subset:
			best = opt(best, costs[(cities[idx], elem)] + g[(elem, frozenset(set(subset).difference({elem})))])
		g[(cities[idx], frozenset(subset))] = best
		best_path = opt(best_path, best)
	return best_path


if __name__ == "__main__":

	# Part 1 Solution
	
	# cost 'matrix' in form of
	# ('start', 'dest') : cost
	costs = dict()
	cities = set()
	
	with open("day9_input", "r") as infile:
		for line in infile.readlines():
			route, cost = line.strip().split(" = ")
			start, dest = route.split(" to ")
			cities.add(dest.strip())
			cities.add(start.strip())
			costs[(start.strip(), dest.strip())] = int(cost)
			costs[(dest.strip(), start.strip())] = int(cost) # symmetric costs

	cities = list(cities) # no more additions, allow for indexing
	
	print dp_tsp(cities, costs, min)
	
	# Part 2 Solution
	
	print dp_tsp(cities, costs, max)
	



