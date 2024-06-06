
import sys

#sys.stdin = open('in.txt', 'r')

n, k, q = map(int, input().split())

left = [None]*n
right = [None]*n

for i in range(n):
    left[i], right[i] = map(int, input().split())

dp = [0]*(200000+1)
for i in range(n):
    dp[left[i]] += 1
    dp[right[i]+1] -= 1

for i in range(1, 200000+1):
    dp[i] = dp[i-1] + dp[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])
