
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    dp = [10**9 for _ in range(max(b) + 1)]
    dp[0] = 0
    for i in range(len(dp)):
        if dp[i] < 10**9:
            for j in a:
                dp[i+j] = min(dp[i+j], dp[i] + 1)
    
    return [dp[x] if dp[x] < 10**9 else -1 for x in b]

print(*solve(a, b), sep="\n")

