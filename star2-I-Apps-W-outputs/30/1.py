
def solve(A, B, n, x):
    res = 0
    while n > 0:
        if n & 1:
            res = (A * x + B) % (10**9 + 7)
        A = (A * A) % (10**9 + 7)
        B = (A * B + B) % (10**9 + 7)
        n >>= 1
    return res

A, B, n, x = map(int, input().split())
print(solve(A, B, n, x))

