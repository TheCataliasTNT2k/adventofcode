with open("inputs/4") as f:
    liste = f.read().strip().splitlines()


def one():
    s = 0
    for line in liste:
        first, second = line.split(",")
        ffn, fsn = list(map(int, first.split("-")))
        sfn, ssn = list(map(int, second.split("-")))
        if ffn >= sfn and fsn <= ssn or \
                ffn <= sfn and fsn >= ssn:
            s += 1
    print(s)


def two():
    s = 0
    for line in liste:
        first, second = line.split(",")
        ffn, fsn = list(sorted(map(int, first.split("-"))))
        sfn, ssn = list(sorted(map(int, second.split("-"))))
        if sfn <= ffn <= ssn or sfn <= fsn <= ssn or \
                ffn <= sfn <= fsn or ffn <= ssn <= fsn:
            s += 1
    print(s)


if __name__ == '__main__':
    two()
