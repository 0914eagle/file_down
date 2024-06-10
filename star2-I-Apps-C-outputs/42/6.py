
def solve(S):
    def f(n):
        return len(str(n))
    
    dp = [[0] * (S + 1) for _ in range(10)]
    for i in range(1, 10):
        dp[i][f(i)] = 1
    
    for i in range(1, 10):
        for j in range(1, S + 1):
            for k in range(i, 10):
                dp[i][j] += dp[k][j - f(i)]
    
    return sum(dp[i][S] for i in range(1, 10)) % (10**9 + 7)

if __name__ == '__main__':
    S = int(input())
    print(solve(S))

