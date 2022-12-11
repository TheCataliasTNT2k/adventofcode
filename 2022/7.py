with open("inputs/7") as f:
    liste = f.read().splitlines()


class File:
    parent: "File" = None
    children: list["File"] = []
    is_dir = False
    size = 0
    name = ""

    def __init__(self, parent: "File", is_dir: bool, name: str, size = 0):
        self.parent = parent
        self.is_dir = is_dir
        self.name = name
        self.size = size
        self.children = []

    def calc_dir_size(self):
        for child in self.children:
            self.size += child.calc_dir_size()
        return self.size

    def calc_size_sum(self):
        if not self.is_dir:
            return 0
        s = 0
        if self.size <= 100000:
            s += self.size
        for child in self.children:
            s += child.calc_size_sum()
        return s

    def find_smallest_dir_to_delete(self, target):
        size = self.size
        if not self.is_dir:
            return 10000000000
        for child in self.children:
            size = min(size, child.find_smallest_dir_to_delete(target))
        if size >= target:
            return size
        return 10000000000


def traverse_tree() -> File:
    root = File(None, True, "/")
    node = root
    mode = 0
    for line in liste:
        if line.startswith("$"):
            mode = 0
        if line == "$ cd /":
            continue
        if mode == 1:
            split = line.split()
            if split[0] == "dir":
                node.children.append(File(node, True, split[1]))
            else:
                node.children.append(File(node, False, split[1], int(split[0])))
        if line == "$ ls":
            mode = 1
        if line.startswith("$ cd"):
            para = line.split()[-1]
            if para == "..":
                node = node.parent
            else:
                node = list(filter(lambda x: x.name == para, node.children))[0]
    return root


def one():
    tree = traverse_tree()
    tree.calc_dir_size()
    print(tree.calc_size_sum())


def two():
    tree = traverse_tree()
    tree.calc_dir_size()
    print(tree.find_smallest_dir_to_delete(30000000 - (70000000 - tree.size)))


if __name__ == '__main__':
    two()
