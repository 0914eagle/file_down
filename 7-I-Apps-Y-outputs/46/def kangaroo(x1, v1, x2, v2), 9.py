
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return -1
    if x1 > x2 and v1 > v2:
        return -1
    if v1 == v2:
        return -1
    if x1 == x2:
        return 0
    if x1 > x2:
        x1, x2 = x2, x1
        v1, v2 = v2, v1
    if v1 > v2:
        return -1
    t = (x2 - x1) / (v1 - v2)
    if t == int(t):
        return int(t)
    return -1

