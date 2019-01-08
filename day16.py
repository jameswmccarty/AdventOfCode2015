#!/usr/bin/python
"""

--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

    children, by human DNA age analysis.
    cats. It doesn't differentiate individual breeds.
    Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
    goldfish. No other kinds of fish.
    trees, all in one group.
    cars, presumably by exhaust or gasoline or something.
    perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

"""

def eq(x,y):
	return x == y

def gt(x,y):
	return x > y

def lt(x,y):
	return x < y


class Sue:

	options = { "children" : eq, "cats" : gt, "samoyeds" : eq, "pomeranians" : lt, "akitas" : eq, "vizslas" : eq, "goldfish" : lt, "trees" : gt, "cars" : eq, "perfumes" : eq }

	def __init__(self, *argv, **kwargs):
		for key, value in kwargs.iteritems():
			if key in self.options:
				setattr(self, key, int(value))
				
	def match(self, items):
		for item in items:
			if hasattr(self, item) and getattr(self, item) != items[item]:
				return False
		return True
		
	def match2(self, items):
		for item in items:
			if hasattr(self, item) and not self.options[item](getattr(self, item), items[item]):
				return False
		return True

if __name__ == "__main__":

	# Part 1 Solution

	all_sue = []

	unk_sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,  "cars": 2, "perfumes": 1 }
	
	with open("day16_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(",")
			first = line[0].split(":")
			second = line[1].split(":")
			third = line[2].split(":")
			kwargs = { first[1].strip():first[2].strip(), second[0].strip():second[1].strip(), third[0].strip():third[1].strip() }
			all_sue.append(Sue(**kwargs))
			
	for idx, sue in enumerate(all_sue):
		if sue.match(unk_sue):
			print idx + 1
			
	# Part 2 Solution

	for idx, sue in enumerate(all_sue):
		if sue.match2(unk_sue):
			print idx + 1
