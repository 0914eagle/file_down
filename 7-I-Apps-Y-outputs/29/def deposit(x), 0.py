
def deposit(x):
    year = 0
    while True:
        year += 1
        x += x//100
        if x >= x:
            break
    return year

