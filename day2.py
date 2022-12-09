def get_input_name():
	return __file__.split("/")[-1].split(".")[0] + ".txt"

def read_input():
	with open(get_input_name(), "r") as f:
		return f.read()


SCORES = {"A X": 4, "A Y": 8, "A Z": 3, 
		  "B X": 1, "B Y": 5, "B Z": 9,
		  "C X": 7, "C Y": 2, "C Z": 6}


SCORES2 = {"A X": 3, "A Y": 4, "A Z": 8, 
		  "B X": 1, "B Y": 5, "B Z": 9,
		  "C X": 2, "C Y": 6, "C Z": 7}


def part1():
	x = list(filter(len, read_input().split("\n")))
	total = 0

	for i, round in enumerate(x):
		total += SCORES[round]

	return total


def part2():
	x = list(filter(len, read_input().split("\n")))
	total = 0

	for i, round in enumerate(x):
		total += SCORES2[round]

	return total


if __name__ == "__main__":
	print(part2())