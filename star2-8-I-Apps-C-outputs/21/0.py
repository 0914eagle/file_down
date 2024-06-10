
def solve(n, k, a):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j >= a[i - 1]:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - a[i - 1]]) % 1000000007
            else:
                dp[i][j] = dp[i - 1][j]
    
    if dp[-1][-1] == 0:
        return [-1, 0]
    
    ways = [[0] * (k + 1) for _ in range(n + 1)]
    ways[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            if j >= a[i - 1]:
                ways[i][j] = (ways[i - 1][j] + ways[i - 1][j - a[i - 1]]) % 1000000007
            else:
                ways[i][j] = ways[i - 1][j]
    
    return [dp[-1][-1], ways[-1][-1]]

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    res = solve(n, k, a)
    print(res[0])
    print(res[1])

if __name__ == '__main__':
    main()

