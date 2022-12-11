with open("inputs/9") as f:
    liste = f.read().strip().splitlines()


def move(nots, c, d, a):
    for _ in range(a):
        match d:
            case "R":
                nots[0][0] += 1
            case "U":
                nots[0][1] -= 1
            case "D":
                nots[0][1] += 1
            case "L":
                nots[0][0] -= 1
        for i in range(len(nots) - 1):
            h = nots[i]
            t = nots[i + 1]
            if abs(t[0] - h[0]) > 1 and abs(t[1] - h[1]) > 1:
                if t[0] < h[0] - 1:
                    t[0] = h[0] - 1
                elif t[0] > h[0] + 1:
                    t[0] = h[0] + 1
                if t[1] < h[1] - 1:
                    t[1] = h[1] - 1
                elif t[1] > h[1] + 1:
                    t[1] = h[1] + 1
            if t[0] < h[0] - 1:
                t[0] = h[0] - 1
                t[1] = h[1]
            elif t[0] > h[0] + 1:
                t[0] = h[0] + 1
                t[1] = h[1]
            elif t[1] < h[1] - 1:
                t[0] = h[0]
                t[1] = h[1] - 1
            elif t[1] > h[1] + 1:
                t[0] = h[0]
                t[1] = h[1] + 1
        c.add((t[0], t[1]))
    return nots, c


def one():
    coords = {(0, 0)}
    nots = [[0, 0] for _ in range(2)]
    for line in liste:
        s = line.split()
        nots, coords = move(nots, coords, s[0], int(s[1]))
    print(len(coords))


def two():
    coords = {(0, 0)}
    nots = [[0, 0] for _ in range(10)]
    for line in liste:
        s = line.split()
        nots, coords = move(nots, coords, s[0], int(s[1]))
    print(len(coords))


if __name__ == '__main__':
    two()
