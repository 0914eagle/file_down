
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'NO'
    else:
        if (x2 - x1) % (v2 - v1) == 0:
            return 'NO'
        else:
            return (x2 - x1) / (v2 - v1)


print(kangaroo(0, 3, 4, 2))

