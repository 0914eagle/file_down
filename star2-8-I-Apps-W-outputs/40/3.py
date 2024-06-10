
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(n, m, a, b):
    return "YES" if len(set(a + b)) < n + m else "NO"

print(solve(n, m, a, b))

