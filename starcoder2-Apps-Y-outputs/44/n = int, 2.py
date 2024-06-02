
n = int(input())
a = list(map(int, input().split()))

# dp[i] = max number of problems in the contest
#        which ends with the i-th problem
dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[j] * 2 >= a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

