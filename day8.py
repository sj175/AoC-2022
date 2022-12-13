def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


def get_column(matrix, j):
    """gets jth column"""
    return [matrix[i][j] for i, _ in enumerate(matrix)]


def is_visible(matrix, i, j) -> bool:
    right = matrix[i][j + 1:]
    left = matrix[i][:j]
    up = get_column(matrix, j)[:i]
    down = get_column(matrix, j)[i + 1:]

    return any((
        all(x < matrix[i][j] for x in right),
        all(x < matrix[i][j] for x in left),
        all(x < matrix[i][j] for x in up),
        all(x < matrix[i][j] for x in down)
    ))


def calc_viewing_distance(direction, tree) -> int:
    if not direction:
        return 0
    for i in range(len(direction)):
        if direction[i] >= tree:
            break

    return i + 1


def get_scenic_score(matrix, i, j) -> int:
    right = matrix[i][j + 1:]
    left = matrix[i][:j]
    up = get_column(matrix, j)[:i]
    down = get_column(matrix, j)[i + 1:]

    return calc_viewing_distance(right, matrix[i][j]) * calc_viewing_distance(left[::-1],
                                                                              matrix[i][j]) * calc_viewing_distance(
        up[::-1], matrix[i][j]) * calc_viewing_distance(down, matrix[i][j])


def part1() -> int:
    input_strings = [list(x) for x in filter(len, read_input().split("\n"))]
    matrix = [list(map(int, x)) for x in input_strings]
    total = 0

    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if is_visible(matrix, i, j):
                total += 1

    return total


def part2() -> int:
    input_strings = [list(x) for x in filter(len, read_input().split("\n"))]
    matrix = [list(map(int, x)) for x in input_strings]
    max_viewing_distance = 0

    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            max_viewing_distance = max(max_viewing_distance, get_scenic_score(matrix, i, j))

    return max_viewing_distance


if __name__ == "__main__":
    print(part1())
    print(part2())
