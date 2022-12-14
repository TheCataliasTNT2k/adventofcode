with open("inputs/14") as f:
    liste = f.read().strip().splitlines()


def sim_sand(infinity: bool):
    # all "rocks"
    rocks = set()
    # lowest "rock" we know
    greatest_y = 0
    # read rocks and add them to "rocks"
    for line in liste:
        # last added rock
        last_coord = []
        # read x and y coordinate for each "wall", for all "walls" within one line
        for x, y in map(lambda c: list(map(int, c.split(","))), line.split(" -> ")):
            # if we do not have a "rock" in this "wall" yet, save the first one
            if not last_coord:
                last_coord = [x, y]
                rocks.add((x, y))
                continue
            # when "wall" is sideways, step one "rock" sideways
            if x != last_coord[0]:
                movement = (max(-1, min(1, x - last_coord[0])), 0)
            # else, step one "rock" up or down
            else:
                movement = (0, max(-1, min(1, y - last_coord[1])))
            # save the coords of the actual "rock" and add this "rock" to the set of known rocks
            while tuple(last_coord) != (x, y):
                last_coord[0] += movement[0]
                last_coord[1] += movement[1]
                # update the lowest known "rock"
                greatest_y = max(greatest_y, last_coord[1])
                rocks.add(tuple(last_coord))
    # when sand should not fall to infinity, we need a "bottom"
    if not infinity:
        # add a "bottom"
        # it needs to be at least as long as the height difference between the "sand spawner" and the bottem we create
        for x in range(500 - greatest_y - 3, 500 + greatest_y + 3):
            # the "bottom" should be 2 tiles lower than the lowest rock
            rocks.add((x, greatest_y + 2))
    # save all blocked tiles
    blocked = set(rocks)
    # how much sand can we "store"?
    amount = 0
    while True:
        # start at the "sand spawner"
        sand = [500, 0]
        while True:
            # save last position of sand piece, so we can compare it later to the actual position
            last_sand = list(sand)
            # move the sandpiece according to the rules
            if (sand[0], sand[1] + 1) not in blocked:
                sand[1] += 1
            elif (sand[0] - 1, sand[1] + 1) not in blocked:
                sand[0] -= 1
                sand[1] += 1
            elif (sand[0] + 1, sand[1] + 1) not in blocked:
                sand[0] += 1
                sand[1] += 1
            # if the sane piece is stuck at the "spawner", we are done
            if sand == [500, 0]:
                return amount + 1
            # if the sand piece did not move during this iteration, we can calculate the next one
            if sand == last_sand:
                amount += 1
                blocked.add(tuple(sand))
                break
            # if the sand falls into the void, we are done
            if sand[1] > greatest_y and infinity:
                return amount


def one():
    print(sim_sand(True))


def two():
    print(sim_sand(False))


if __name__ == '__main__':
    two()
