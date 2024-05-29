
def count_special_numbers(n, k):
    def count_bits(num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    # Helper function to calculate nCr % mod
    def nCr(n, r, mod):
        if r > n - r:
            r = n - r
        result = 1
        for i in range(r):
            result = (result * (n - i)) % mod
            result = (result * pow(i + 1, mod - 2, mod)) % mod
        return result

    mod = 10 ** 9 + 7
    dp = [[0] * (k + 1) for _ in range(1010)]
    cnt = 0

    for i in range(1010):
        num_bits = count_bits(i)
        dp[i][num_bits] = 1

    for i in range(1, 1010):
        for j in range(1010):
            dp[i][j] = (dp[i][j] + dp[i - 1][j] + dp[i - 1][j - 1]) % mod

    for i in range(1, n + 1):
        bits = count_bits(i)
        if dp[i][bits] == k:
            cnt = (cnt + 1) % mod

    return cnt

n = int(input(), 2)
k = int(input())
result = count_special_numbers(n, k)
print(result)
```
