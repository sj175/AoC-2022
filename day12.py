from collections import namedtuple

the_input = []
Point = namedtuple("Point", "label value path_length i j previous")


def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


def read_test_input():
    return """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def main(start, end, part, test_input):
    global the_input
    input_func = read_test_input if test_input else read_input
    the_input = list(map(list, filter(len, input_func().split("\n"))))

    for i, row in enumerate(the_input):
        for j, elem in enumerate(row):
            if elem == start:
                start_i = i
                start_j = j

    return bfs(start_i, start_j, end, part, test_input)


def replace_E_with_z(i, j):
    repl = {"E": "z", "S": "a"}
    return the_input[i][j] if the_input[i][j] not in repl.keys() else repl[the_input[i][j]]


def get_connected(current, test_input):
    i = current.i
    j = current.j
    path_length = current.path_length
    output = []
    test_i_max = 4
    test_j_max = 7
    main_i_max = 40
    main_j_max = 153
    i_max = test_i_max if test_input else main_i_max
    j_max = test_j_max if test_input else main_j_max

    if i > 0:
        value = replace_E_with_z(i - 1, j)
        output.append(Point(the_input[i - 1][j], value, path_length + 1, i - 1, j, current))
    if i < i_max:
        value = replace_E_with_z(i + 1, j)
        output.append(Point(the_input[i + 1][j], value, path_length + 1, i + 1, j, current))
    if j > 0:
        value = replace_E_with_z(i, j - 1)
        output.append(Point(the_input[i][j - 1], value, path_length + 1, i, j - 1, current))
    if j < j_max:
        value = replace_E_with_z(i, j + 1)
        output.append(Point(the_input[i][j + 1], value, path_length + 1, i, j + 1, current))

    return output


def comparison(part, elem_value, current_value):
    if part == 1:
        return ord(elem_value) <= ord(current_value) + 1
    elif part == 2:
        return ord(elem_value) >= ord(current_value) - 1
    else:
        raise ValueError("expected 1 or 2 for part")


def bfs(start_i, start_j, end_value, part, test_input):
    queue = [Point(the_input[start_i][start_j], replace_E_with_z(start_i, start_j), 0, start_i, start_j, None)]
    seen = set()
    while queue:
        current = queue.pop(0)
        for elem in get_connected(current, test_input):
            if comparison(part, elem.value, current.value):
                if elem.label == end_value:
                    return elem
                if (elem.i, elem.j) not in seen:
                    queue.append(elem)
                    seen.add((elem.i, elem.j))

    raise ValueError("Didn't find end point!")


def part1():
    return main("S", "E", 1, False).path_length


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
    use_example_input = False
    main_columns = 154
    main_rows = 41
    example_columns = 8
    example_rows = 5
    rows = example_rows if use_example_input else main_rows
    columns = example_columns if use_example_input else main_columns

    output = [["."] * columns for _ in range(rows)]
    final = main("E", "a", 2, use_example_input)
    print(final.path_length)
    current = final
    output[final.i][final.j] = "E"

    while current.previous:
        output[current.previous.i][current.previous.j] = get_direction(current.previous, current)
        current = current.previous

    for row2 in output:
        print(''.join(row2))


if __name__ == "__main__":
    print("path length: ", part1())
    print("*****")
    part2()
