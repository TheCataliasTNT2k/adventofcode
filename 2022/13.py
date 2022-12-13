from functools import cmp_to_key
from json import loads

with open("inputs/13") as f:
    liste = f.read().strip().splitlines()


def compare_lists(list1: list | int, list2: list | int) -> int:
    # if both integer, compare
    if isinstance(list1, int) and isinstance(list2, int):
        return max(-1, min(1, list1 - list2))
    # make integers to list
    if isinstance(list1, int):
        list1 = [list1]
    if isinstance(list2, int):
        list2 = [list2]

    # iterate over lists
    i = 1
    while True:
        # if left list empty
        if len(list1) < i:
            # if both lists empty
            if len(list1) == len(list2):
                return 0
            return -1
        # if right list empty
        if len(list2) < i:
            # if both lists empty
            if len(list1) == len(list2):
                return 0
            return 1
        # both lists have value at i -1, compare them
        res = compare_lists(list1[i - 1], list2[i - 1])
        # elements at i - 1 not equal, return result
        if res != 0:
            return res
        i += 1


def one():
    right = 0
    j = 1
    # calc order for all lists
    for i in range(len(liste) // 3 + 1):
        if compare_lists(loads(liste[3 * i]), loads(liste[3 * i + 1])) == -1:
            right += j
            print(j)
        j += 1
    print(right)


def two():
    lists = []
    # put all lists in file in one big list
    for line in liste:
        if line != "":
            lists.append(loads(line))

    # add markers
    lists.append([2])
    lists.append([6])

    #sort the big list and print result
    lists = sorted(lists, key=cmp_to_key(compare_lists))
    print((lists.index([2]) + 1) * (lists.index([6]) + 1))


if __name__ == '__main__':
    two()
