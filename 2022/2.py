with open("inputs/2") as f:
    liste = f.read().strip().splitlines()


def calc_outcome(game):
    games = {"A X": 4, "A Y": 8, "A Z": 3,
             "B X": 1, "B Y": 5, "B Z": 9,
             "C X": 7, "C Y": 2, "C Z": 6}
    return games[game]


def get_counterpart(game):
    games = {"A X": "A Z", "A Y": "A X", "A Z": "A Y",
             "B X": "B X", "B Y": "B Y", "B Z": "B Z",
             "C X": "C Y", "C Y": "C Z", "C Z": "C X"}
    return games[game]


def one():
    print(sum([calc_outcome(f) for f in liste]))


def two():
    print(sum([calc_outcome(get_counterpart(f)) for f in liste]))


if __name__ == '__main__':
    two()
