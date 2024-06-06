
n = int(input())
dp = [0]*n
for i in range(n):
    s = input()
    for j in range(i):
        if dp[j] == 1:
            continue
        l = len(s) + len(s) - dp[j]
        if l >= len(s):
            k = l - len(s)
            if s[k:] == s[:l - k]:
                dp[i] += 1
                dp[j] += 1
print(sum(dp))
