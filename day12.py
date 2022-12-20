from collections import namedtuple

the_input = []
Point = namedtuple("Point", "value path_length i j previous")


def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


def read_input_2():
    return """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def main(start, end):
    global the_input
    the_input = list(map(list, filter(len, read_input_2().split("\n"))))

    for i, row in enumerate(the_input):
        for j, elem in enumerate(row):
            if elem == start:
                start_i = i
                start_j = j

    return bfs(start_i, start_j, end)


def get_connected(current):
    i = current.i
    j = current.j
    path_length = current.path_length
    output = []
    if i > 0:
        output.append(Point(the_input[i - 1][j], path_length + 1, i - 1, j, current))
    if i < 4:
        output.append(Point(the_input[i + 1][j], path_length + 1, i + 1, j, current))
    if j > 0:
        output.append(Point(the_input[i][j - 1], path_length + 1, i, j - 1, current))
    if j < 7:  # 153:
        output.append(Point(the_input[i][j + 1], path_length + 1, i, j + 1, current))

    return output


def bfs(start_i, start_j, end_value):
    queue = [Point("a", 0, start_i, start_j, None)]
    seen = set()
    while queue:
        current = queue.pop(0)
        for elem in get_connected(current):
            if ord(elem.value) <= ord(current.value) + 1:
                if elem.value == end_value:
                    return elem
                if (elem.i, elem.j) not in seen:
                    queue.append(elem)
                    seen.add((elem.i, elem.j))

    raise ValueError("Didn't find end point!")


def part1():
    return main("S", "E")


def is_adjacent(a, b):
    return any((
        (a.i == b.i) and (-1 <= abs(a.j - b.j) <= 1),
        (a.j == b.j) and (-1 <= abs(a.i - b.i) <= 1)
    ))


def get_direction(a, b):
    """direction to get from a to b"""
    assert is_adjacent(a, b)
    if a.i > b.i:
        return "^"
    elif a.i < b.i:
        return "v"
    elif a.j > b.j:
        return "<"
    elif a.j < b.j:
        return ">"


def part2():
    output = [["."] * 8 for _ in range(5)]
    final = main("S", "E")
    print(final.path_length)
    current = final
    output[final.i][final.j] = "E"

    # for i, row in enumerate(the_input):
    #     for j, elem in enumerate(row):
    #         if i == final.i and j == final.j:
    #             output[i][j] = "E"
    #         else:
    #             output[i][j] = "."

    while current.previous:
        # print(current, current.previous)
        output[current.previous.i][current.previous.j] = get_direction(current.previous, current)
        current = current.previous

    for row2 in output:
        print(''.join(row2))


if __name__ == "__main__":
    # print(part1())
    print("*****")
    print(part2())

# 177 too low
