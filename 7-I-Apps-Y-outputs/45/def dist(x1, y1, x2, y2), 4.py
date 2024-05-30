
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    gopher = [float(x) for x in input().split()]
    dog = [float(x) for x in input().split()]
    holes = []
    for i in range(int(input())):
        holes.append([float(x) for x in input().split()])

    min_dist = float('inf')
    hole = None
    for hole in holes:
        dist_dog = dist(hole[0], hole[1], dog[0], dog[1])
        dist_gopher = dist(hole[0], hole[1], gopher[0], gopher[1])
        if dist_dog < dist_gopher:
            if dist_dog < min_dist:
                min_dist = dist_dog
                hole = hole
        elif dist_gopher < min_dist:
            min_dist = dist_gopher
            hole = hole
    if hole is not None:
        print("The gopher can escape through the hole at ({0}, {1}).".format(hole[0], hole[1]))
    else:
        print("The gopher cannot escape.")

if __name__ == "__main__":
    main()

