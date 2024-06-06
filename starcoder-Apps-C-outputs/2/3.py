
def solve(n, d, c, a, b):
    a = set(a)
    b = set(b)
    total = 0
    for _ in range(n):
        c = min(c, len(a), len(b))
        x = c
        if c != 0:
            while x < d:
                x = x + c
                c = c - 1
            total = total + x
        if len(a) == 0 or len(b) == 0:
            break
        if c == 0:
            break
        x = a.intersection(b)
        a = a.difference(x)
        b = b.difference(x)
    if len(a) != 0 or len(b) != 0:
        c = min(c, len(a), len(b))
        total = total + c
    return total

if __name__ == '__main__':
    n, d, c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solve(n, d, c, a, b))
