
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    for i in range(1, n):
        ans += a[i]
    print(ans)

q = int(input())
for _ in range(q):
    solve()

