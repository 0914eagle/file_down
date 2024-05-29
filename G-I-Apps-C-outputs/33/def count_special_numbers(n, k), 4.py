
def count_special_numbers(n, k):
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(1, k + 1):
        dp[i] = dp[i - 1] * (k - i + 1) // i

    def count_ones(x):
        return bin(x).count('1')

    def dfs(x, bits):
        if x == 1:
            return bits == 1

        if bits == 1:
            return x == 2

        count = count_ones(x)
        ans = 0
        for i in range(k - count + 1):
            ans = (ans + dfs(dp[count] * x, count + i)) % (10**9 + 7)
        
        return ans

    return dfs(int(n, 2), 0)

# Input parsing
n = input()
k = int(input())

result = count_special_numbers(n, k)
print(result)
```
