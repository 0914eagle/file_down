
def any_int(x, y, z):
    if x == y + z and x.is_integer():
        return True
    elif y == x + z and y.is_integer():
        return True
    elif z == x + y and z.is_integer():
        return True
    else:
        return False
 