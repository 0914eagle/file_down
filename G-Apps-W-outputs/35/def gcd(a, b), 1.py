
MOD = 10**9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_sequences(x, y):
    if y % x != 0:
        return 0
    
    y //= x
    
    dp = [0] * (y + 1)
    dp[0] = 1
    
    for i in range(1, y + 1):
        for j in range(i, y + 1, i):
            dp[j] = (dp[j] + dp[j - i]) % MOD
            
    return dp[-1]

x, y = map(int, input().split())
result = count_sequences(x, y)
print(result)
