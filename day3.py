def get_input_name():
	return __file__.split("/")[-1].split(".")[0] + ".txt"

def read_input():
	with open(get_input_name(), "r") as f:
		return f.read()


def get_priority(char: str) -> int:
	if 97 <= ord(char) <= 122:
		return ord(char) - 96
	elif 65 <= ord(char) <= 90:
		return ord(char) - 38
	else:
		raise Exception(f"unexpected character: {char}")


def part1() -> int:
	x = list(filter(len, read_input().split("\n")))
	total = 0

	for backpack in x:
		total += get_priority(list(set(backpack[len(backpack)//2:]).intersection(backpack[:len(backpack)//2]))[0])

	return total




def part2() -> int:
	x = list(filter(len, read_input().split("\n")))
	total = 0

	for i in range(0, len(x), 3):
		badge = list(set(x[i]).intersection(x[i+1]).intersection(x[i+2]))
		total += get_priority(badge[0])

	return total


if __name__ == "__main__":
	print(part2())