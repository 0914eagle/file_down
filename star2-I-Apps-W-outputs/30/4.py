
def solve(a, b, n, x):
    res = 0
    while n > 0:
        if n & 1:
            res = (a * x + b) % (10**9 + 7)
        a = (a * a) % (10**9 + 7)
        b = (a * b + b) % (10**9 + 7)
        n >>= 1
    return res


if __name__ == '__main__':
    a, b, n, x = map(int, input().split())
    print(solve(a, b, n, x))

