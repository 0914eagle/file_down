
import math
def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def main():
    gopher = [float(i) for i in input().split()]
    dog = [float(i) for i in input().split()]
    holes = []
    for i in range(int(input())):
        holes.append([float(i) for i in input().split()])
    for hole in holes:
        if distance(hole[0],hole[1],gopher[0],gopher[1]) < distance(hole[0],hole[1],dog[0],dog[1]):
            print("The gopher can escape through the hole at ({0},{1}).".format(hole[0],hole[1]))
            return
    print("The gopher cannot escape.")
main()

