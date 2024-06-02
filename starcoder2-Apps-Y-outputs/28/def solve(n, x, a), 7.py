
def solve(n, x, a):
    ans = 0
    for i in range(1, n):
        if a[i] + a[i - 1] > x:
            ans += a[i] + a[i - 1] - x
            a[i] = x - a[i - 1]
    return ans

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, x, a))

