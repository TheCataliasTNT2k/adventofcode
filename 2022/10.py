with open("inputs/10") as f:
    liste = f.read().strip().splitlines()


def one():
    cycle = 1
    register = 1
    c_num = 0
    i = 0
    values = {1: 1}
    while True:
        line = liste[i]
        if c_num == 1:
            c_num = 0
            register += int(line.split()[1])
        elif line.startswith("addx"):
            c_num = 1
            i -= 1
        cycle += 1
        values.update({cycle: register})
        i += 1
        if i == len(liste):
            break
    s = sum([values[f] * f for f in [20, 60, 100, 140, 180, 220]])
    print(s)


def two():
    cycle = 1
    register = 1
    c_num = 0
    i = 0
    counter = 0
    values = {1: 1}
    string = ""
    while True:
        if counter % 40 == 0 and counter > 0:
            string += "\n"
        if register == counter % 40 or register - 1 == counter % 40 or register + 1 == counter % 40:
            string += "#"
        else:
            string += "."
        line = liste[i]
        if c_num == 1:
            c_num = 0
            register += int(line.split()[1])
        elif line.startswith("addx"):
            c_num = 1
            i -= 1
        cycle += 1
        counter += 1
        values.update({cycle: register})
        i += 1
        if i == len(liste):
            break
    print(string)


if __name__ == '__main__':
    two()
