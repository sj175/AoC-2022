def get_input_name() -> str:
    return __file__.split("/")[-1].split(".")[0] + ".txt"


def read_input():
    with open(get_input_name(), "r") as f:
        return f.read()


class Node:
    def __init__(self, value, file_type, children, parent=None):
        if children:
            self.children = children
        else:
            self.children = []
        if parent:
            self.parent = parent

        self.value = value
        self.file_type = file_type

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
        dirs = []

        if not self.children:
            return self.value
        else:
            child_dirs = list(filter(lambda x: x.file_type == "dir", self.children))
            if child_dirs:
                for child in child_dirs:
                    dirs.append(child.get_directories())
            else:
                return self.value

        return dirs


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
            if line.startswith("dir"):
                print("adding child")
                filename = line.split(" ")[1]
                current.add_child(Node(filename, "dir", [], current))
                print(current)
                print(current.children)
            else:
                current.add_child(Node(filename, "file", [], current))

    return root.get_directories()


# def main() -> int:
# 	the_input = filter(len, read_input().split("\n"))
# 	state = defaultdict(list)
# 	current = ""
# 	current_dir = state[current]

# 	for line in the_input:
# 		print(line)
# 		if line.startswith("$"):
# 			command = line.split("$ ")[1]
# 			if command.startswith("ls"):
# 				pass
# 			elif command.startswith("cd"):
# 				dir_name = command.split(" ")[1]
# 				if dir_name == "/":
# 					current = "/"
# 				elif dir_name == "..":
# 					current = ''.join(dir_name[:-len(dir_name.split("/")[-2])-1])
# 				else:
# 					current += command.split(" ")[1] + "/"
# 					current_dir = state[current]

# 		else:
# 			current_dir.append(line)

# 	return state


def part1() -> int:
    return main()


def part2() -> int:
    return main()


if __name__ == "__main__":
    print(part1())
# print(part2())
