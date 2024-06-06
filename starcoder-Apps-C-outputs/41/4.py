
n = int(input())
times = list(map(int, input().split()))
graph = {}
for i in range(n):
    graph[i+1] = list(map(int, input().split()))[1:]

dp = [0 for i in range(n+1)]
for i in range(1, n+1):
    for j in graph[i]:
        dp[i] = max(dp[i], dp[j])
    dp[i] += times[i-1]

print(dp[-1])
