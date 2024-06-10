
def solve(a, b):
    return "YES" if a == b else "NO"

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

print(solve(a, b))

