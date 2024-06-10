
def solve(k, a):
    n = 7
    days = [0] * n
    for i in range(n):
        days[i] = a[i] * (i + 1)
    days = sorted(days)
    ans = 0
    for i in range(n):
        if days[i] > 0:
            ans += days[i]
            k -= 1
        if k == 0:
            break
    return ans

t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    print(solve(k, a))

