#!/usr/bin/python

"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

--- Part Two ---

You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

Although it hasn't changed, you can still get your puzzle input.

"""

def adj_on(x, y, grid):
	count = 0
	for j in range(max(0,y-1),min(len(grid),y+2)):
		for i in range(max(0,x-1),min(len(grid[0]),x+2)):
			if not (i==x and j==y) and grid[j][i]== '#':
				count += 1
	return count
	
def count_on(grid):
	count = 0
	for row in grid:
		count += row.count("#")
	return count
	
def print_grid(grid):
	for row in grid:
		print ''.join(row)
	print
	
def next_grid(grid):
	next_gen = []
	for y, row in enumerate(grid):
		next_row = []
		for x, char in enumerate(row):
			nc = '.'
			adj = adj_on(x, y, grid)
			if char == '#' and (adj == 2 or adj == 3):
				nc = '#'
			elif char == '.' and adj == 3:
				nc = '#'
			next_row.append(nc)
		next_gen.append(next_row)
	return next_gen		

	
if __name__ == "__main__":

	# Part 1 Solution
	
	grid = []
	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			grid.append(list(line.strip()))
			
	for i in range(100):
		#print_grid(grid)
		grid = next_grid(grid)
	print count_on(grid)
	
	# Part 2 Solution
	grid = []
	
	with open("day18_input", "r") as infile:
		for line in infile.readlines():
			grid.append(list(line.strip()))
	# Turn on corners
	grid[0][0] = '#'
	grid[len(grid)-1][0] = '#'
	grid[0][len(grid[0])-1] = '#'
	grid[len(grid)-1][len(grid[0])-1] = '#'
	for i in range(100):
		#print_grid(grid)
		grid = next_grid(grid)
		grid[0][0] = '#'
		grid[len(grid)-1][0] = '#'
		grid[0][len(grid[0])-1] = '#'
		grid[len(grid)-1][len(grid[0])-1] = '#'
	print count_on(grid)
	
	
