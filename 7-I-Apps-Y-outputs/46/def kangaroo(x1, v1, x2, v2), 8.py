
def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO'
    elif (x2 - x1) % (v1 - v2) == 0:
        return 'NO'
    else:
        return 'YES'

