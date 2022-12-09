def get_input_name():
	return __file__.split("/")[-1].split(".")[0] + ".txt"

def read_input():
	with open(get_input_name(), "r") as f:
		return f.read()


def detect_full_contains(range1, range2) -> bool:
	range1_start = int(range1.split("-")[0])
	range1_end = int(range1.split("-")[1])
	range2_start = int(range2.split("-")[0])
	range2_end = int(range2.split("-")[1])

	if range1_start >= range2_start and range1_end <= range2_end:
		return True
	elif range2_start >= range1_start and range2_end <= range1_end:
		return True
	else:
		return False

def detect_overlap(range1, range2) -> bool:
	range1_start = int(range1.split("-")[0])
	range1_end = int(range1.split("-")[1])
	range2_start = int(range2.split("-")[0])
	range2_end = int(range2.split("-")[1])

	if range1_start >= range2_start and range1_start <= range2_end:
		return True
	elif range2_start >= range1_start and range2_start <= range1_end:
		return True
	else:
		return False


def main(func) -> int:
	x = list(filter(len, read_input().split("\n")))
	total = 0

	for i, pair in enumerate(x):
		if func(pair.split(",")[0], pair.split(",")[1]):
			total += 1

	return total


def part1() -> int:
	return main(detect_full_contains)


def part2() -> int:
	return main(detect_overlap)

if __name__ == "__main__":
	print(part2())