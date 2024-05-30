
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def escape(gopher, dog, holes):
    for hole in holes:
        if distance(gopher[0], gopher[1], hole[0], hole[1]) < distance(dog[0], dog[1], hole[0], hole[1]):
            return "The gopher can escape through the hole at ({0}, {1}).".format(hole[0], hole[1])
    return "The gopher cannot escape."

def main():
    gopher = list(map(float, input().split()))
    dog = list(map(float, input().split()))
    holes = []
    for i in range(int(input())):
        holes.append(list(map(float, input().split())))
    print(escape(gopher, dog, holes))

if __name__ == "__main__":
    main()

