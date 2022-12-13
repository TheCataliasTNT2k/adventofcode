with open("inputs/12") as f:
    liste = f.read().strip().splitlines()


def get_shortest_path(start, stop_char, reverse=False):
    length = len(liste)
    width = len(liste[0])
    # all found nodes with parents
    nodes = {}
    # nodes to check this round
    to_work: list[tuple[int, int]] = []
    # nodes to check next round (BFS)
    to_work_next_round: list[tuple[int, int]] = []
    # already visited nodes (already in nodes or will be checked within the next round)
    visited_nodes = set()
    # last node
    end = None
    # init start of tree
    nodes.update({start: [None, start]})
    to_work.append(start)
    # run while we have nodes to check and end has not been found yet
    while len(to_work) > 0 and not end:
        for k in to_work:
            # actual node was definitely checked now
            visited_nodes.add(k)
            letter = liste[k[1]][k[0]]

            # "repair" wrong letters
            if letter == "S":
                letter = "a"
            elif letter == "E":
                letter = "z"

            # iterate over all adjacent nodes
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x2, y2 = k[0] + dx, k[1] + dy
                # prevent out of bounds conditions
                if x2 < 0 or x2 + 1 > width or y2 < 0 or y2 + 1 > length:
                    continue

                new_letter = liste[y2][x2]
                found = False
                if new_letter == stop_char:
                    found = True
                # "repair" wrong letters
                if new_letter == "S":
                    new_letter = "a"
                elif new_letter == "E":
                    new_letter = "z"

                # check if we can go to the adjacent node, ignore already checked ones
                if reverse:  # allow multiple "up"
                    if ord(letter) - ord(new_letter) > 1 or (x2, y2) in visited_nodes:
                        continue
                else:  # allow multiple "down"
                    if ord(new_letter) - ord(letter) > 1 or (x2, y2) in visited_nodes:
                        continue

                # we found our target, stop here
                if found:
                    nodes.update({(x2, y2): [k, (x2, y2)]})
                    end = (x2, y2)
                    break

                # add adjacent node to nodes and queue it for next round
                if not nodes.get((x2, y2)):
                    visited_nodes.add((x2, y2))
                    to_work_next_round.append((x2, y2))
                    nodes.update({(x2, y2): [k, (x2, y2)]})
        # switch working sets for next round
        to_work = to_work_next_round
        to_work_next_round = list()

    # calc path length
    num = 0
    while end:
        end = nodes.get(end)[0]
        num += 1
    return num - 1


def one():
    start = None
    # find starting point
    for i in range(len(liste)):
        if "S" in liste[i]:
            start = (liste[i].index("S"), i)
            break
    print(get_shortest_path(start, "E"))


def two():
    start = None
    # find starting point
    for i in range(len(liste)):
        if "E" in liste[i]:
            start = (liste[i].index("E"), i)
            break
    print(get_shortest_path(start, "a", True))


if __name__ == '__main__':
    two()
