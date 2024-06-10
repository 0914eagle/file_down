
def solve(A, B, n, x):
    res = 1
    while n:
        if n & 1:
            res = (A * res + B) % (10**9 + 7)
        A = (A * A + B) % (10**9 + 7)
        B = (A * B + B) % (10**9 + 7)
        n >>= 1
    return res

A, B, n, x = map(int, input().split())
print(solve(A, B, n, x))

