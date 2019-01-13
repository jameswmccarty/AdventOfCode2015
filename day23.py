#!/usr/bin/python

"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some unknown benefactor. It comes with instructions and an example program, but the computer itself seems to be malfunctioning. She's curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

    hlf r sets register r to half its current value, then continues with the next instruction.
    tpl r sets register r to triple its current value, then continues with the next instruction.
    inc r increments register r, adding 1 to it, then continues with the next instruction.
    jmp offset is a jump; it continues with the instruction offset away relative to itself.
    jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a

What is the value in register b when the program in your puzzle input is finished executing?

--- Part Two ---

The unknown benefactor is very thankful for releasi-- er, helping little Jane Marie with her computer. Definitely not to distract you, what is the value in register b after the program is finished executing if register a starts as 1 instead?

"""

regs = { "a" : 0, "b" : 0, "ip" : -1 }

def hlf(r, o):
	regs[r] = int(regs[r] / 2)
	
def tpl(r, o):
	regs[r] *= 3
	
def inc(r, o):
	regs[r] += 1

def jie(r, o):
	if regs[r] % 2 == 0:
		regs["ip"] += int(o)-1

def jio(r, o):
	if regs[r] == 1:
		regs["ip"] += int(o)-1

def jmp(r, o):
	regs["ip"] += int(r)-1

if __name__ == "__main__":

	# Part 1 Solution

	program = []
	op = { "hlf" : hlf, "tpl" : tpl, "inc" : inc, "jie" : jie, "jio" : jio, "jmp" : jmp }
	
	with open("day23_input", "r") as infile:
		for line in infile.readlines():
			line = line.split(" ")
			if len(line) < 3 and len(line) > 1:
				line.append(".")
			line = [ x.strip().strip(",") for x in line ]
			program.append(line)

	while regs["ip"] < len(program)-1:
		regs["ip"] += 1
		op[program[regs["ip"]][0]](program[regs["ip"]][1], program[regs["ip"]][2])

	print regs["b"]
	
