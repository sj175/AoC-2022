def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


def main() -> int:
    return None


def part1() -> int:
    return None


def part2() -> int:
    return None


if __name__ == "__main__":
    print(part1())
    # print(part2())
