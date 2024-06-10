
def solve(S):
    def f(n):
        return len(str(n))
    
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(1, S + 1):
        for j in range(1, 10):
            if i - f(j) >= 0:
                dp[i] += dp[i - f(j)]
    
    return dp[S] % (10**9 + 7)

S = int(input())
print(solve(S))

