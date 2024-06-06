
def solution(s):
    n = len(s)
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if s[i] > s[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

s = input()
print(solution(s))
