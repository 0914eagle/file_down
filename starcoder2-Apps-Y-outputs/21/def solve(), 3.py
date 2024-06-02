
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 0
    for i in range(n):
        if i < k:
            ans += max(a[i], b[n-i-1])
        else:
            ans += a[i]
    return ans

t = int(input())
for i in range(t):
    print(solve())

