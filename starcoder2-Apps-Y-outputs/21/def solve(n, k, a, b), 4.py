
def solve(n, k, a, b):
    a.sort()
    b.sort()
    if k % 2 == 1:
        a[0], b[-1] = b[-1], a[0]
    return sum(a)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, k, a, b))

