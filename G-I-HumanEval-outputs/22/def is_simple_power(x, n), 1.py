
def is_simple_power(x, n):
    if x == 1:
        return n == 1
    if x == 0 or n == 1:
        return False
    power = 1
    while power < x:
        power *= n
    return power == x
