
n = int(input())
x = list(map(int, input().split()))
x.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if (x[i] - x[j]) & (x[i] - x[j] - 1) == 0:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

last = dp.index(max(dp))
subset = [x[last]]
for i in range(last, 0, -1):
    if dp[i] == dp[i - 1] + 1:
        subset.append(x[i - 1])
        last = i - 1

print(*subset[::-1])

