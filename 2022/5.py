import re

with open("inputs/5") as f:
    liste = f.read().splitlines()


def one():
    stacks = {}
    list2 = []
    mode = 0
    amount_of_stacks = 0
    for line in liste:
        if line.startswith(" 1 "):
            mode = 1
            for line2 in reversed(list2):
                for i, content in enumerate(line2.replace("    ", " ").split(" "), start=1):
                    if content == "":
                        continue
                    content = content.replace("[", "").replace("]", "")
                    amount_of_stacks = max(i, amount_of_stacks)
                    stack = stacks.get(i) or []
                    stack.append(content)
                    stacks[i] = stack
            continue
        if mode == 0:
            list2.append(line)
        elif line != "":
            m = re.match(r"move (\d*) from (\d*) to (\d*)", line)
            if not m:
                print("Error ", line)
                exit(0)
            amount = int(m.groups()[0])
            from_stack = int(m.groups()[1])
            to_stack = int(m.groups()[2])
            for _ in range(amount):
                stacks[to_stack].append(stacks[from_stack].pop())
    print("".join([stacks[f].pop() or "" for f in range(1, amount_of_stacks + 1)]))


def two():
    stacks = {}
    list2 = []
    mode = 0
    amount_of_stacks = 0
    for line in liste:
        if line.startswith(" 1 "):
            mode = 1
            for line2 in reversed(list2):
                for i, content in enumerate(line2.replace("    ", " ").split(" "), start=1):
                    if content == "":
                        continue
                    content = content.replace("[", "").replace("]", "")
                    amount_of_stacks = max(i, amount_of_stacks)
                    stack = stacks.get(i) or []
                    stack.append(content)
                    stacks[i] = stack
            continue
        if mode == 0:
            list2.append(line)
        elif line != "":
            m = re.match(r"move (\d*) from (\d*) to (\d*)", line)
            if not m:
                print("Error ", line)
                exit(0)
            amount = int(m.groups()[0])
            from_stack = int(m.groups()[1])
            to_stack = int(m.groups()[2])
            crates = []
            for _ in range(amount):
                crates.append(stacks[from_stack].pop())
            for crate in reversed(crates):
                stacks[to_stack].append(crate)
    print("".join([stacks[f].pop() or "" for f in range(1, amount_of_stacks + 1)]))


if __name__ == '__main__':
    two()
