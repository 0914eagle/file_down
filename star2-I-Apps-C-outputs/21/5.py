
def solve(n, k, a):
    a.sort()
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] % a[j] != k:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))

