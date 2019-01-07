#!/usr/bin/python

import itertools

"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?


"""

# algorithm for generating interger partitions of fixed size k
# generator function
def partition_k(n, k):
	if n <= 1:
		return 
	if k <= 0:
		return 
	part = [0] * k
	part[0] = (n-k) + 1
	for i in range(1,k):
		part[i] = 1
	yield part
	yielded = True
	while yielded:
		yielded = False
		for i in range(k):
			if part[i] < part[0]-1:
				yielded = True
				for j in range(1,i+1):
					part[j] = part[i]+1
				part[0] = n - sum(part[1:])
				yield part
				break

class Ingredient:

	def __init__(self, capacity, durability, flavor, texture, calories):
		self.traits = [capacity, durability, flavor, texture, calories]
		
def score_cookie(ingredients, measures):
	sub_scores = [0] * 4
	for i in range(4):
		for idx, amount in enumerate(measures):
			sub_scores[i] += amount * ingredients[idx].traits[i]
	sub_scores = [ max(x,0) for x in sub_scores ]
	return reduce(lambda x, y: x*y, sub_scores)
	
def score_cookie_cal(ingredients, measures):
	sub_scores = [0] * 5
	for i in range(5):
		for idx, amount in enumerate(measures):
			sub_scores[i] += amount * ingredients[idx].traits[i]
	sub_scores = [ max(x,0) for x in sub_scores ]
	if sub_scores[4] != 500:
		return 0
	else:
		sub_scores[4] = 1
	return reduce(lambda x, y: x*y, sub_scores)	
		
if __name__ == "__main__":

	ingredients = []
	# Part 1 Solution
	with open("day15_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			ingredients.append(Ingredient(int(line[2].strip(",")), int(line[4].strip(",")), int(line[6].strip(",")), int(line[8].strip(",")), int(line[10].strip())))

	highest_score = 0
	for x in partition_k(100,len(ingredients)):
		for y in itertools.permutations(x):
			highest_score = max(highest_score, score_cookie(ingredients, y))
	print highest_score
	
	# Part 2 Solution
	highest_score = 0
	for x in partition_k(100,len(ingredients)):
		for y in itertools.permutations(x):
			highest_score = max(highest_score, score_cookie_cal(ingredients, y))
	print highest_score
