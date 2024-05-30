
def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 0
    if v1 == v2:
        return -1
    if v1 > v2:
        return -1
    if v1 == v2 and x1 < x2:
        return -1
    if v1 == v2 and x1 > x2:
        return -1
    return (x2 - x1) / (v1 - v2)



