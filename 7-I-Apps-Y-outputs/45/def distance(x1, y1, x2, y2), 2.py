
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def escape(gopher, dog, holes):
    min_distance = float('inf')
    for hole in holes:
        d = distance(gopher[0], gopher[1], hole[0], hole[1])
        if d < min_distance:
            min_distance = d
            hole_x = hole[0]
            hole_y = hole[1]
    if min_distance < distance(gopher[0], gopher[1], dog[0], dog[1]):
        print("The gopher can escape through the hole at ({0}, {1}).".format(hole_x, hole_y))
    else:
        print("The gopher cannot escape.")


if __name__ == '__main__':
    gopher = [float(x) for x in input().split()]
    dog = [float(x) for x in input().split()]
    holes = []
    for i in range(int(input())):
        holes.append([float(x) for x in input().split()])
    escape(gopher, dog, holes)

