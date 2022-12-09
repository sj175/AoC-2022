def get_input_name():
	return __file__.split("/")[-1].split(".")[0] + ".txt"

def read_input():
	with open(get_input_name(), "r") as f:
		return f.read()


def part1():
	x = read_input().split("\n")
	largest_elf = 0
	current_elf = 0
	for food_item in x:
		if food_item != "":
			current_elf += int(food_item)
		else:
			largest_elf = max(largest_elf, current_elf)
			current_elf = 0

	return largest_elf

def transform(x):
	return sum(map(int, filter(len, x.split("\n"))))


def part2():
	x = read_input().split("\n\n")
	x = sorted(map(transform, x), reverse=True)

	return sum(x[:3])


if __name__ == "__main__":
	print(part2())