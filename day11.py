def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


class Monkey:
    def __init__(self, items, operation, test_by):
        self.items = items
        self.operation = operation
        self.test_by = test_by
        self.inspection_count = 0


def main(rounds) -> int:
    monkey_0 = Monkey([66, 79], lambda x: x * 11, [7, 6, 7])
    monkey_1 = Monkey([84, 94, 94, 81, 98, 75], lambda x: x * 17, [13, 5, 2])
    monkey_2 = Monkey([85, 79, 59, 64, 79, 95, 67], lambda x: x + 8, [5, 4, 5])
    monkey_3 = Monkey([70], lambda x: x + 3, [19, 6, 0])
    monkey_4 = Monkey([57, 69, 78, 78], lambda x: x + 4, [2, 0, 3])
    monkey_5 = Monkey([65, 92, 60, 74, 72], lambda x: x + 7, [11, 3, 4])
    monkey_6 = Monkey([77, 91, 91], lambda x: x * x, [17, 1, 7])
    monkey_7 = Monkey([76, 58, 57, 55, 67, 77, 54, 99], lambda x: x + 6, [3, 2, 1])
    monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                item_worry_level = monkey.operation(item)
                item_worry_level %= (2*3*5*7*11*13*17*19)
                if item_worry_level % monkey.test_by[0] == 0:
                    monkeys[monkey.test_by[1]].items.append(item_worry_level)
                else:
                    monkeys[monkey.test_by[2]].items.append(item_worry_level)
                monkey.inspection_count += 1
            monkey.items = []

    highest = sorted(map(lambda x: x.inspection_count, monkeys))[-2:]
    return highest[0]*highest[1]


def part1() -> int:
    return main(20)


def part2():
    return main(10000)


if __name__ == "__main__":
    print(part1())
    print("*****")
    print(part2())
