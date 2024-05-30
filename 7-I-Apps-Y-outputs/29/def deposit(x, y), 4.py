
def deposit(x, y):
    if x >= y:
        return 0
    else:
        return 1 + deposit(x * 1.01, y)

def deposit_year(x, y):
    return deposit(100, y)


