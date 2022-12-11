with open("inputs/6") as f:
    line = f.readline().strip()


def one():
    l = []
    for i in range(len(line)):
        l.append(line[i])
        if len(l) > 4:
            l.pop(0)
        if len(set(l)) >= 4:
            print(i + 1)
            break


def two():
    l = []
    for i in range(len(line)):
        l.append(line[i])
        if len(l) > 14:
            l.pop(0)
        if len(set(l)) >= 14:
            print(i + 1)
            break


if __name__ == '__main__':
    two()
