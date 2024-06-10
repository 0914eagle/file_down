
def solve():
    n, m = map(int, input().split())
    s = [0] * n
    x = [0.0] * n
    for i in range(n):
        s[i], x[i] = map(int, input().split())
    last = [0.0] * m
    for i in range(n):
        if last[s[i] - 1] < x[i]:
            last[s[i] - 1] = x[i]
    ans = 0
    for i in range(m):
        if last[i] == 0.0:
            ans += 1
    print(ans)
solve()

