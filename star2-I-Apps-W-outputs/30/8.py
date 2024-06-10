
def solve(A, B, n, x):
    res = 0
    for i in range(64):
        if (n >> i) & 1:
            res = (A * res + B) % (10**9 + 7)
    return res
A, B, n, x = map(int, input().split())
print(solve(A, B, n, x))

