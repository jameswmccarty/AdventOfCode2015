#!/usr/bin/python

"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

"""

signals = {}

def emulate(instructions):
	global signals
	while len(instructions) > 0:
		for inst in instructions:
			if "AND" in inst[0]:
				a,b = inst[0].split(" AND ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = a & b & 0xFFFF
					instructions.remove(inst)
			elif "OR" in inst[0]:
				a,b = inst[0].split(" OR ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = (a | b) & 0xFFFF
					instructions.remove(inst)
			elif "LSHIFT" in inst[0]:
				a,b = inst[0].split(" LSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] << int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "RSHIFT" in inst[0]:
				a,b = inst[0].split(" RSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] >> int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "NOT" in inst[0]:
				a = inst[0].replace("NOT ", '')
				if a in signals:
					signals[inst[1]] = ~signals[a] & 0xFFFF
					instructions.remove(inst)
			else:
				a = inst[0]
				if a in signals:
					signals[inst[1]] = signals[a]	
					instructions.remove(inst)
				else:
					try:
						a = int(a)
						signals[inst[1]] = a
						instructions.remove(inst)
					except:
						continue

def emulate_ovr(instructions):
	global signals
	while len(instructions) > 0:
		for inst in instructions:
			signals['b'] = 3176
			if "AND" in inst[0]:
				a,b = inst[0].split(" AND ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = a & b & 0xFFFF
					instructions.remove(inst)
			elif "OR" in inst[0]:
				a,b = inst[0].split(" OR ")
				if a in signals:
					a = signals[a]
				else:
					try:
						a = int(a)
					except:
						a = None
				if b in signals:
					b = signals[b]
				else:
					try:
						b = int(b)
					except:
						b = None				
				if a != None and b != None:
					signals[inst[1]] = (a | b) & 0xFFFF
					instructions.remove(inst)
			elif "LSHIFT" in inst[0]:
				a,b = inst[0].split(" LSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] << int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "RSHIFT" in inst[0]:
				a,b = inst[0].split(" RSHIFT ")
				if a in signals:
					signals[inst[1]] = (signals[a] >> int(b)) & 0xFFFF
					instructions.remove(inst)
			elif "NOT" in inst[0]:
				a = inst[0].replace("NOT ", '')
				if a in signals:
					signals[inst[1]] = ~signals[a] & 0xFFFF
					instructions.remove(inst)
			else:
				a = inst[0]
				if a in signals:
					signals[inst[1]] = signals[a]	
					instructions.remove(inst)
				else:
					try:
						a = int(a)
						signals[inst[1]] = a
						instructions.remove(inst)
					except:
						continue

if __name__ == "__main__":

	# Part 1 Solution

	instructions = []	
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			instructions.append(line.strip().split(" -> "))	
	emulate(instructions)						
	print signals['a']
	
	# Part 2 Solution
	instructions = []	
	signals = {}
	with open("day7_input", "r") as infile:
		for line in infile.readlines():
			instructions.append(line.strip().split(" -> "))
	emulate_ovr(instructions)
	print signals['a']
	

	
