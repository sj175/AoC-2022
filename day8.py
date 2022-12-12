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


def main() -> int:
    input_strings = [list(x) for x in filter(len, read_input().split("\n"))]
    matrix = [list(map(int, x)) for x in input_strings]
    total = 0

    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if is_visible(matrix, i, j):
                total += 1

    return total


def part1() -> int:
    return main()


def part2() -> int:
    return main()


if __name__ == "__main__":
    print(part1())
    # print(part2())
