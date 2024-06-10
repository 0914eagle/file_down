
n = int(input())
a = list(map(int, input().split()))

def f(l, r):
    return r - l + 1

ans = 0
for l in range(1, n + 1):
    for r in range(l, n + 1):
        ans += f(l, r)

print(ans)

