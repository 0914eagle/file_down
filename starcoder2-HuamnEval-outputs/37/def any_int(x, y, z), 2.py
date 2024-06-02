
def any_int(x, y, z):
    if x == y + z and type(x) == int and type(y) == int and type(z) == int:
        return True
    elif x + y == z and type(x) == int and type(y) == int and type(z) == int:
        return True
    elif x + z == y and type(x) == int and type(y) == int and type(z) == int:
        return True
    else:
        return False
 