
def gopher(gopher_coords, dog_coords, holes):
    gopher_x, gopher_y = gopher_coords
    dog_x, dog_y = dog_coords
    gopher_hole = None
    for hole in holes:
        hole_x, hole_y = hole
        if (hole_x - gopher_x)**2 + (hole_y - gopher_y)**2 < (hole_x - dog_x)**2 + (hole_y - dog_y)**2:
            gopher_hole = hole
            break
    if gopher_hole is None:
        print("The gopher cannot escape.")
    else:
        print("The gopher can escape through the hole at ({:.3f}, {:.3f}).".format(*gopher_hole))

if __name__ == "__main__":
    gopher_coords = [float(x) for x in input().split()]
    dog_coords = [float(x) for x in input().split()]
    holes = []
    for _ in range(int(input())):
        holes.append([float(x) for x in input().split()])
    gopher(gopher_coords, dog_coords, holes)

