
def solve(N, x, a):
    ans = 0
    for i in range(N-1):
        if a[i] + a[i+1] > x:
            ans += a[i] + a[i+1] - x
            a[i+1] = x - a[i]
    return ans

N, x = map(int, input().split())
a = list(map(int, input().split()))
print(solve(N, x, a))

