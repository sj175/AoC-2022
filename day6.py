def get_input_name() -> str:
	return __file__.split("/")[-1].split(".")[0] + ".txt"

def read_input():
	with open(get_input_name(), "r") as f:
		return f.read()


def main(signal, magic_number) -> int:
	for i in range(magic_number, len(signal)):
		if len(set(signal[i-magic_number:i])) == magic_number:
			return i

	return None


def part1() -> int:
	return main(read_input(), 4)


def part2() -> int:
	return main(read_input(), 14)

if __name__ == "__main__":
	print(part1())
	print(part2())