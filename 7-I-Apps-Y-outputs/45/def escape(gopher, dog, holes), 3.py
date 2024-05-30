
import math
def escape(gopher, dog, holes):
    gopher_x, gopher_y = gopher
    dog_x, dog_y = dog
    gopher_hole_x, gopher_hole_y = holes[0]
    dog_hole_x, dog_hole_y = holes[1]
    gopher_dist = math.sqrt((gopher_x - gopher_hole_x)**2 + (gopher_y - gopher_hole_y)**2)
    dog_dist = math.sqrt((dog_x - dog_hole_x)**2 + (dog_y - dog_hole_y)**2)
    if gopher_dist < dog_dist:
        return "The gopher can escape through the hole at ({}, {})".format(gopher_hole_x, gopher_hole_y)
    else:
        return "The gopher cannot escape"

