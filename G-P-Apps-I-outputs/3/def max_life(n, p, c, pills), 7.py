
import sys

def max_life(n, p, c, pills):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] + 1
        for pill in pills:
            t, x, y = pill
            if i >= t:
                dp[i] = max(dp[i], dp[i-t] + x - y)
        if i > 0:
            dp[i] = max(dp[i], dp[i-1] - c)
    return dp[n]

if __name__ == "__main__":
    n, p, c = map(int, input().split())
    pills = []
    for _ in range(p):
        t, x, y = map(int, input().split())
        pills.append((t, x, y))
    result = max_life(n, p, c, pills)
    print("{:.10f}".format(result))
```
