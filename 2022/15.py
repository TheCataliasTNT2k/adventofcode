import re
from itertools import chain

with open("inputs/15") as f:
    liste = f.read().strip().splitlines()


def one():
    # line to count occupied fields in
    line_to_process = 2000000
    # this fields in "line_to_process" are seen by a sensor or occupied by a beacon
    known_fields_at_line = set()
    # store known beacons found in "line_to_process"
    known_beacons_at_line = set()
    # for all sensors
    for line in liste:
        # parse line
        match = re.search(r"(-?\d*), .*?(-?\d*):[\S\s]*?(-?\d*), .*?(-?\d*)$", line)
        s_x = int(match.groups()[0])
        s_y = int(match.groups()[1])
        b_x = int(match.groups()[2])
        b_y = int(match.groups()[3])
        # if we have a beacon in our "Line_to_process", save it
        if b_y == line_to_process:
            known_beacons_at_line.add(b_x)
        # how far in each non-diagonal can this sensor see?
        sensor_radius = abs(s_x - b_x) + abs(s_y - b_y)
        # how many fields can this sensor see in the "line_to_process"?
        remaining_at_line = sensor_radius - abs(line_to_process - s_y)
        # add all fields seen by the sensor to "known_fields_at_line"
        for i in range(remaining_at_line + 1):
            known_fields_at_line.add(s_x - i)
            known_fields_at_line.add(s_x + i)
    # subtract beacons in "line_to_process" from occupied fields
    print(f"{len(known_fields_at_line.difference(known_beacons_at_line))} fields can not be a beacon.")


class Sensor:
    # store position
    x: int
    y: int
    # store radius
    radius: int

    def __init__(self, x, y, b_x, b_y):
        self.x = x
        self.y = y
        self.radius = abs(x - b_x) + abs(y - b_y)

    def get_borders_by_y(self, y: int):
        # calculate borders of range the sensor can see in this line
        if self.radius - abs(self.y - y) >= 0:
            dx = self.radius - abs(self.y - y)
            return self.x - dx, self.x + dx
        # if sensor can not see any field in this line, return None
        if self.radius - abs(self.y - y) < 0:
            return None


def two():
    # stop searching here
    y_border = 4000000
    # store all known sensors
    sensors = []
    # for all sensors
    for line in liste:
        # parse line
        match = re.search(r"(-?\d*), .*?(-?\d*):[\S\s]*?(-?\d*), .*?(-?\d*)$", line)
        s_x = int(match.groups()[0])
        s_y = int(match.groups()[1])
        b_x = int(match.groups()[2])
        b_y = int(match.groups()[3])
        # save sensor
        sensors.append(Sensor(s_x, s_y, b_x, b_y))
    print("Searching")
    # search on each line for a field which is not seen by any sensor
    for y in range(y_border):
        # get all ranges of all sensors, which can see at least one field in this line
        ranges = sorted(filter(lambda x: x != (), [s.get_borders_by_y(y) or () for s in sensors]), key=lambda x: x[0])
        # go from left to right through the ranges
        added_range = []
        for r in ranges:
            # init "added_range"
            if not added_range:
                added_range = list(r)
            else:
                # when this range overlaps the oder one, "expand" the saved one
                if added_range[0] <= r[0] <= added_range[1] + 1:
                    added_range[1] = max(added_range[1], r[1])
                # it does not? we found an empty spot
                else:
                    print(f"The tuning frequency is {(added_range[1] + 1) * 4000000 + y}.")
                    return


def two_but_faster():
    # this code is from
    # https://github.com/Defelo/AdventOfCode/blob/master/2022/15.py,
    # but I commented it, so it is better understandable

    # read all sensors and beacons in a list of tuples: list[(tuple(sensor_x, sensor_y, beacon_x, beacon_y)]
    inp = [tuple([int(x[0]) for x in re.finditer(r"[+-]?\d+", line)]) for line in liste]
    # storage for sensors
    sensors = []
    # limits for search window
    minx = 1e1337
    miny = 1e1337
    maxx = -1e1337
    maxy = -1e1337
    for sx, sy, bx, by in inp:
        # how far in each non-diagonal can this sensor see?
        sensor_radius = abs(sx - bx) + abs(sy - by)
        # store sensor
        sensors.append((sx, sy, sensor_radius))

        # limit search window
        minx = min(sx, minx)
        miny = min(sy, miny)
        maxx = max(sx, maxx)
        maxy = max(sy, maxy)

    for sx, sy, sensor_radius in sensors:
        # iterate over the fields of the diagonal borders of this sensor,
        #   but "move the border one field away from the sensor"
        for x, y in chain(
            iter_line(sx, sy - sensor_radius - 1, sx + sensor_radius + 1, sy),
            iter_line(sx + sensor_radius + 1, sy, sx, sy + sensor_radius + 1),
            iter_line(sx, sy + sensor_radius + 1, sx - sensor_radius - 1, sy),
            iter_line(sx - sensor_radius - 1, sy, sx, sy - sensor_radius - 1),
        ):
            # when the field is inside our search window
            # and no sensor can see this field
            #   (use the radius of the other sensors to check, if it is one or within their borders)
            if minx <= x <= maxx and miny <= y <= maxy and \
                    all(abs(x - a) + abs(y - b) > d for a, b, d in sensors):
                # hey, we found our x and y value
                return x * 4000000 + y


def iter_line(x1, y1, x2, y2):
    # https://github.com/Defelo/AdventOfCode/blob/9ae5127981b024eaa0fd694607f200626701f5d0/utils/grid.py#L43
    xr = range(min(x1, x2), max(x1, x2) + 1)
    if x1 > x2:
        xr = xr[::-1]

    yr = range(min(y1, y2), max(y1, y2) + 1)
    if y1 > y2:
        yr = yr[::-1]

    if x1 == x2:
        xr = [x1] * len(yr)
    if y1 == y2:
        yr = [y1] * len(xr)

    for x, y in zip(xr, yr):
        yield x, y


if __name__ == '__main__':
    two()
