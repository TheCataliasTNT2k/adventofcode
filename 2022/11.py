import re

with open("inputs/11") as f:
    liste = f.read()


class Monkey:
    number: int
    items: list[int]
    operator: str
    change_value: str
    divider: int
    true: int
    false: int
    processed_items: int
    worry_divider: int = 3

    def __init__(self, number: int, items: list[int], operator: str, value: str, divider: int, true: int, false: int,
                 worry_divider: int = 3):
        self.number = number
        self.items = items
        self.operator = operator
        self.change_value = value
        self.divider = divider
        self.true = true
        self.false = false
        self.processed_items = 0
        self.worry_divider = worry_divider

    def do(self, ml: list["Monkey"], cmd: int = 1):
        for item in self.items:
            self.processed_items += 1
            second = item if self.change_value == "old" else int(self.change_value)
            item = item * second if self.operator == "*" else item + second
            item //= self.worry_divider
            item %= cmd
            if item % self.divider == 0:
                ml[self.true].items.append(item)
            else:
                ml[self.false].items.append(item)
        self.items = []


def one():
    ml: list[Monkey] = []
    for m in re.finditer(r"(Monkey (\d*):\n .*: ([\d, ]*)\n .*= old (.) (.*)\n .*by (\d*)\n .*monkey (\d*)\n .*monkey (\d*))", liste):
        ml.append(Monkey(
            int(m.groups()[1]),
            list(map(int, m.groups()[2].split(", "))),
            m.groups()[3],
            m.groups()[4],
            int(m.groups()[5]),
            int(m.groups()[6]),
            int(m.groups()[7])
        ))
    for _ in range(20):
        for m in ml:
            m.do(ml)
    sml = list(sorted(ml, key=lambda m: -m.processed_items))
    print(sml[0].processed_items * sml[1].processed_items)


def two():
    ml: list[Monkey] = []
    for m in re.finditer(r"(Monkey (\d*):\n .*: ([\d, ]*)\n .*= old (.) (.*)\n .*by (\d*)\n .*monkey (\d*)\n .*monkey (\d*))", liste):
        ml.append(Monkey(
            int(m.groups()[1]),
            list(map(int, m.groups()[2].split(", "))),
            m.groups()[3],
            m.groups()[4],
            int(m.groups()[5]),
            int(m.groups()[6]),
            int(m.groups()[7]),
            1
        ))
    cmd = 1
    s = set()
    for m in ml:
        s.add(m.divider)
    for i in s:
        cmd *= i
    for i in range(10000):
        for m in ml:
            m.do(ml, cmd)
    sml = list(sorted(ml, key=lambda m: -m.processed_items))
    print(sml[0].processed_items * sml[1].processed_items)


if __name__ == '__main__':
    two()
