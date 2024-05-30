
def stomach(x, a, b):
    if b <= x:
        return "safe"
    elif a <= x + 1:
        return "dangerous"
    else:
        return "delicious"

