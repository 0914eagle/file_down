
def any_int(x, y, z):
    return (x == y + z or y == x + z or z == x + y) and (x % 1 == 0 and y % 1 == 0 and z % 1 == 0)
 