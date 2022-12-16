def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


SIGNAL_CYCLES = [20, 60, 100, 140, 180, 220]


def check_signal_strength(signal_strengths, cycle, x):
    if cycle in SIGNAL_CYCLES:
        signal_strengths.append(cycle * x)


SCREEN_BUFFER = [["."] * 40 for _ in range(6)]


def draw(register, cycle):
    if (register - 1) <= (cycle - (40 * (cycle // 40)) - 1) <= (register + 1):
        SCREEN_BUFFER[(cycle - 1) // 40][(cycle - 1) % 40] = "#"


def main(the_input) -> int:
    instructions = filter(len, the_input.split("\n"))
    cycle = 0
    x = 1
    signal_strengths = []

    for instr in instructions:
        if instr.split(" ")[0] == "noop":
            cycle += 1
            check_signal_strength(signal_strengths, cycle, x)
            draw(x, cycle)

        elif instr.split(" ")[0] == "addx":
            cycle += 1
            check_signal_strength(signal_strengths, cycle, x)
            draw(x, cycle)
            cycle += 1
            check_signal_strength(signal_strengths, cycle, x)
            draw(x, cycle)
            x += int(instr.split(" ")[1])

        else:
            raise Exception(f"unrecognised instruction: {instr}")

    return sum(signal_strengths)


def part1() -> int:
    return main(read_input())


def part2():
    main(read_input())


if __name__ == "__main__":
    # print(part1())
    part2()
    for line in SCREEN_BUFFER:
        output = ""
        for char in line:
            output += char
        print(output)
