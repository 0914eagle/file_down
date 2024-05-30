
def gopher(gopher_coords, dog_coords, holes):
    # Write your code here
    gopher_x, gopher_y = gopher_coords
    dog_x, dog_y = dog_coords
    for hole in holes:
        hole_x, hole_y = hole
        if (hole_x - gopher_x) ** 2 + (hole_y - gopher_y) ** 2 < (hole_x - dog_x) ** 2 + (hole_y - dog_y) ** 2:
            return "The gopher can escape through the hole at ({}, {})".format(hole_x, hole_y)
    return "The gopher cannot escape."

