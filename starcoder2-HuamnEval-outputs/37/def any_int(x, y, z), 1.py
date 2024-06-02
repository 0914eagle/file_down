
def any_int(x, y, z):
    if x + y == z and x == int(x) and y == int(y) and z == int(z):
        return True
    elif x + z == y and x == int(x) and y == int(y) and z == int(z):
        return True
    elif y + z == x and x == int(x) and y == int(y) and z == int(z):
        return True
    else:
        return False
 