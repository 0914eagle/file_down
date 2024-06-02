
def any_int(x, y, z):
    if (x+y==z) or (x+z==y) or (y+z==x):
        if (type(x)==int) and (type(y)==int) and (type(z)==int):
            return True
        else:
            return False
    else:
        return False
 