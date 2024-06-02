
def any_int(x, y, z):
    if type(x) == int and type(y) == int and type(z) == int:
        if x == y + z or x == y - z or x == z - y or x + y == z or x - y == z or x + z == y or x - z == y or y + z == x or y - z == x or y + x == z or y - x == z or z + x == y or z - x == y or z + y == x or z - y == x:
            return True
        else:
            return False
    else:
        return False
 