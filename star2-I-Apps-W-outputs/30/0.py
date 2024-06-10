
def solve(A, B, n, x):
    return (A * x + B) % (10**9 + 7)

A, B, n, x = map(int, input().split())
print(solve(A, B, n, x))

