def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


class Node:
    def __init__(self, value, file_type, children, size=0, parent=None):
        if children:
            self.children = children
        else:
            self.children = []
        if parent:
            self.parent = parent

        self.value = value
        self.file_type = file_type
        self.size = size

    def __str__(self):
        return self.file_type + " " + self.value

    def __repr__(self):
        return self.__str__()

    def add_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_child(self, child):
        for potential in self.children:
            if potential.value == child:
                return potential
        raise ValueError(f"Child not found: {child}")

    def get_directories(self):
        dirs = [self]

        for child in self.children:
            if child.file_type == "dir":
                dirs += child.get_directories()

        return dirs

    def get_size(self):
        total = 0

        if not self.children:
            return self.size

        for child in self.children:
            total += child.get_size()

        return total


def main() -> int:
    the_input = filter(len, read_input().split("\n"))
    root = Node("/", "dir", [])
    current = None

    for line in the_input:
        if line.startswith("$"):
            command = line.split("$ ")[1]
            if command.startswith("ls"):
                pass
            elif command.startswith("cd"):
                dir_name = command.split(" ")[1]
                if dir_name == "/":
                    current = root
                elif dir_name == "..":
                    current = current.get_parent()
                else:
                    current = current.get_child(dir_name)

        else:
            filename = line.split(" ")[1]
            if line.startswith("dir"):
                current.add_child(Node(filename, "dir", [], parent=current))
            else:
                current.add_child(Node(filename, "file", [], int(line.split(" ")[0]), current))

    return root.get_directories()


def part1() -> int:
    dirs = main()
    dir_sizes = []
    for dir in dirs:
        dir_sizes.append(dir.get_size())

    return sum(filter(lambda x: x < 100000, dir_sizes))


def part2() -> int:
    return main()


if __name__ == "__main__":
    print(part1() == 1453349)
    print(part2())
