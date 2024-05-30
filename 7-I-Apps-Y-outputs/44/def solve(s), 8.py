

def solve(s):
    n = len(s)
    if n % 2 == 1:
        return -1
    a = s.count('a')
    b = s.count('b')
    if a == b:
        return 0
    if a > b:
        return (a - b) // 2
    else:
        return (b - a) // 2


def solve(s):
    n = len(s)
    if n % 2 == 1:
        return -1
    a = s.count('a')
    b = s.count('b')
    if a == b:
        return 0
    if a > b:
        return (a - b) // 2
    else:
        return (b - a) // 2


