with open("inputs/8") as f:
    liste = f.read().strip().splitlines()


def empty_list(l):
    return [-1 for _ in range(l)]


def one():
    s = set()
    amount = 0
    l = len(liste)
    w = len(liste[0])
    highest_vertical = empty_list(w)
    highest_horizontal = empty_list(w)
    for i in range(l):
        for j in range(w):
            e = int(liste[i][j])
            if e > highest_vertical[j]:
                highest_vertical[j] = e
                if (i, j) not in s:
                    amount += 1
                    s.add((i, j))
            if e > highest_horizontal[i]:
                highest_horizontal[i] = e
                if (i, j) not in s:
                    amount += 1
                    s.add((i, j))
    highest_vertical = empty_list(w)
    highest_horizontal = empty_list(w)
    for i in range(l - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            e = int(liste[i][j])
            if e > highest_vertical[j]:
                highest_vertical[j] = e
                if (i, j) not in s:
                    amount += 1
                    s.add((i, j))
            if e > highest_horizontal[i]:
                highest_horizontal[i] = e
                if (i, j) not in s:
                    amount += 1
                    s.add((i, j))
    print(len(s))


def set_tree(x, y):
    amount = 0
    l = len(liste)
    w = len(liste[0])
    height = int(liste[y][x])
    s = 0
    for i in range(x + 1, w):
        s += 1
        if int(liste[y][i]) >= height:
            break
    amount = s
    s = 0
    for i in range(x - 1, -1, -1):
        s += 1
        if int(liste[y][i]) >= height:
            break
    amount *= s
    s = 0
    for i in range(y + 1, l):
        s += 1
        if int(liste[i][x]) >= height:
            break
    amount *= s
    s = 0
    for i in range(y - 1, -1, -1):
        s += 1
        if int(liste[i][x]) >= height:
            break
    amount *= s

    return amount


def two():
    trees = {}
    l = len(liste)
    w = len(liste[0])
    highest = 0
    for i in range(l):
        for j in range(w):
            trees[(j, i)] = set_tree(j, i)
            if trees[(j, i)] > highest:
                highest = trees[(j, i)]
    print(highest)


if __name__ == '__main__':
    two()
