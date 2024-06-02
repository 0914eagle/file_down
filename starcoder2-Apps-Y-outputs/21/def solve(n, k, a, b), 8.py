
def solve(n, k, a, b):
    a.sort()
    b.sort()
    if k >= n:
        return sum(b)
    return sum(a[n - k:]) + sum(b[:k])

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, k, a, b))

