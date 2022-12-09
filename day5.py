import re
import functools

def get_input_name():
	return __file__.split("/")[-1].split(".")[0] + ".txt"

def read_input():
	with open(get_input_name(), "r") as f:
		return f.read()

def get_starting_state():
	starting_state = read_input().split("\n\n")[0]
	stacks = {}
	for i in range(9):
		stacks[i+1] = []

	for line in starting_state.split("\n")[:-1][::-1]:
		stack = 0
		for i in range(1, 35, 4):
			stack += 1
			if line[i] != " ":
				stacks[stack].append(line[i])

	return stacks

def get_instructions():
	instructions = list(filter(len, read_input().split("\n\n")[1].split("\n")))
	curried_find_all = functools.partial(re.findall, r"\d+")
	numerical_instructions = map(curried_find_all, instructions)

	return map(lambda x: list(map(int, x)), numerical_instructions)


def part1() -> int:
	output = ""
	stacks = get_starting_state()
	instructions = get_instructions()

	for instr in instructions:
		for _ in range(instr[0]):
			stacks[instr[2]].append(stacks[instr[1]].pop())

	for i in range(9):
		output += stacks[i+1][-1]

	return output


def part2() -> int:
	stacks = get_starting_state()
	output = ""
	instructions = get_instructions()

	for instr in instructions:
		for element in stacks[instr[1]][-instr[0]:]:
			stacks[instr[2]].append(element)
		for _ in range(instr[0]):
			stacks[instr[1]].pop()

	for i in range(9):
		output += stacks[i+1][-1]

	return output

if __name__ == "__main__":
	print(part2())