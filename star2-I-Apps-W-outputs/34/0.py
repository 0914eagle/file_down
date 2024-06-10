
def solve(n, k, a):
    d = max(a)
    for i in range(n):
        a[i] = d - a[i]
    return a

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = solve(n, k, a)
    print(*a)

