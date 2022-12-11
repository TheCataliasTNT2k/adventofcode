with open("inputs/3") as f:
    liste = f.read().strip().splitlines()


def one():
    s = 0
    for line in liste:
        first, second = line[:len(line) // 2], line[len(line) // 2:]
        sim = set(first).intersection(set(second)).pop()
        if ord("a") <= ord(sim) <= ord("z"):
            s += ord(sim) - ord("a") + 1
        else:
            s += ord(sim) - ord("A") + 27
    print(s)


def two():
    s = 0
    for i in range(len(liste) // 3):
        sim = {}
        for j in range(3):
            el = liste[i * 3 + j]
            if not sim:
                sim = set(el)
            else:
                sim = set(el).intersection(sim)
        sim = sim.pop()
        if ord("a") <= ord(sim) <= ord("z"):
            s += ord(sim) - ord("a") + 1
        else:
            s += ord(sim) - ord("A") + 27
    print(s)


if __name__ == '__main__':
    two()
