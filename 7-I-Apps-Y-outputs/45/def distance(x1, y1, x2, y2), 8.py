
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_hole(gopher_pos, dog_pos, holes):
    gopher_hole = None
    min_distance = None
    for hole in holes:
        d = distance(gopher_pos[0], gopher_pos[1], hole[0], hole[1])
        if min_distance is None or d < min_distance:
            min_distance = d
            gopher_hole = hole
    return gopher_hole

def main():
    gopher_pos = [float(x) for x in input().split()]
    dog_pos = [float(x) for x in input().split()]
    holes = []
    for _ in range(int(input())):
        holes.append([float(x) for x in input().split()])
    gopher_hole = find_hole(gopher_pos, dog_pos, holes)
    if gopher_hole is not None:
        print("The gopher can escape through the hole at ({}, {})".format(gopher_hole[0], gopher_hole[1]))
    else:
        print("The gopher cannot escape.")

main()

