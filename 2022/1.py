with open("inputs/1") as f:
    liste = []
    s = 0
    for cal in f:
        if cal == "\n":
            liste.append(s)
            s = 0
            continue
        s += int(cal)


def one():
    print(sorted(liste)[-1])


def two():
    print(sorted(liste)[-1] + sorted(liste)[-2] + sorted(liste)[-3])


if __name__ == '__main__':
    two()
