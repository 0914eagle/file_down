
def lexicographically_smaller(a, b):
    if a*b < b*a:
        return a*b
    elif a*b > b*a:
        return b*a
    else:
        return a*b

