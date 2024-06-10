
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    a.sort(reverse=True)
    for i in range(len(a)):
        a[i] = (a[i], i)
    a.sort()
    
    dp = [float('inf')] * (b + 1)
    dp[0] = 0
    
    for i in range(b + 1):
        if dp[i] == float('inf'):
            continue
        for v, idx in a:
            if i + v <= b:
                dp[i + v] = min(dp[i + v], dp[i] + 1)
    
    if dp[b] == float('inf'):
        return -1
    return dp[b]

for x in b:
    print(solve(a, x))

