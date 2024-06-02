
def any_int(x, y, z):
    if x == y + z:
        return True
    elif y == x + z:
        return True
    elif z == x + y:
        return True
    else:
        return False
 