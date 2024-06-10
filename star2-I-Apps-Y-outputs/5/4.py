
n = int(input())
x = list(map(int, input().split()))
x.sort()
dp = [1] * n
for i in range(n):
    for j in range(i):
        if (x[i] - x[j]) & (x[i] - x[j] - 1) == 0:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
print(*[x[i] for i in range(n) if dp[i] == max(dp)])

