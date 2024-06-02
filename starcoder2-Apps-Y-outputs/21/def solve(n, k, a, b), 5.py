
def solve(n, k, a, b):
    a.sort()
    b.sort()
    if k % 2 == 0:
        return sum(a)
    else:
        return sum(a) + sum(b) - min(a[0], b[0])

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, k, a, b))

