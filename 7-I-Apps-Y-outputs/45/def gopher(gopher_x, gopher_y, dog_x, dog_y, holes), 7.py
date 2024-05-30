
import math
def gopher(gopher_x, gopher_y, dog_x, dog_y, holes):
    gopher_hole = []
    for hole in holes:
        hole_x = hole[0]
        hole_y = hole[1]
        gopher_dist = math.sqrt((hole_x - gopher_x)**2 + (hole_y - gopher_y)**2)
        dog_dist = math.sqrt((hole_x - dog_x)**2 + (hole_y - dog_y)**2)
        if gopher_dist < dog_dist:
            gopher_hole.append(hole)
    if len(gopher_hole) == 0:
        print("The gopher cannot escape.")
    else:
        print("The gopher can escape through the hole at ({0}, {1}).".format(gopher_hole[0][0], gopher_hole[0][1]))

gopher_x = float(input())
gopher_y = float(input())
dog_x = float(input())
dog_y = float(input())
n = int(input())
holes = []
for i in range(n):
    holes.append([float(input()), float(input())])
gopher(gopher_x, gopher_y, dog_x, dog_y, holes)

