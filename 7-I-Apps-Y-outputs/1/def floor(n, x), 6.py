
def floor(n, x):
    if n <= 2:
        return 1
    else:
        return floor(n - 2, x) + 1

