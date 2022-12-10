import math


def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


class Rope:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Rope):
            return Rope(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Rope):
            return Rope(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, Rope):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __repr__(self):
        return f"Rope({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.__repr__())


UNIT_DIRECTIONS = {"U": Rope(0, 1), "D": Rope(0, -1), "L": Rope(-1, 0), "R": Rope(1, 0)}


def validate_rules(h: Rope, t: Rope) -> bool:
    diff = h - t
    if math.sqrt(diff.x ** 2 + diff.y ** 2) < 2:
        return True

    return False


def get_new_t(h: Rope, t: Rope) -> Rope:
    diff = h - t
    if (abs(diff.x) == 2) and (diff.y == 0):
        return Rope(t.x + diff.x//2, t.y)

    elif (abs(diff.y) == 2) and (diff.x == 0):
        return Rope(t.x, t.y + diff.y//2)

    elif (abs(diff.x) == 2) and (abs(diff.y) == 1):
        return Rope(t.x + diff.x // 2, t.y + diff.y)

    elif (abs(diff.x) == 1) and (abs(diff.y) == 2):
        return Rope(t.x + diff.x, t.y + diff.y // 2)

    else:
        print("diff: ", diff)
        raise Exception("you fucked up")


def main() -> int:
    moves = filter(len, read_input().split("\n"))
    h = Rope(0, 0)
    t = Rope(0, 0)
    t_destinations = {t}
    for move in moves:
        dir = move.split(" ")[0]
        length = int(move.split(" ")[1])
        for _ in range(length):
            h = h + UNIT_DIRECTIONS[dir]
            if not validate_rules(h, t):
                t = get_new_t(h, t)
                t_destinations.add(t)

    return len(t_destinations)


def part1() -> int:
    return main()


def part2() -> int:
    return main()


if __name__ == "__main__":
    print(part1())
    # print(part2())
