
def solve(n, k, a):
    a.sort()
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[i] % a[j] != 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

