
def solve(n, a, b):
    if n % 2 == 0:
        return n * a
    else:
        return min(n * a, (n // 2 + 1) * b)

q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    print(solve(n, a, b))

