
def count_subsequences(n, m):
    MOD = 10**9 + 7

    def power(x, y):
        res = 1
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % MOD
            y //= 2
            x = (x * x) % MOD
        return res

    def count_subsequences_helper(n, m):
        return (power(m, n) - 1) % MOD

    return count_subsequences_helper(n, m)

# Input
n, m = map(int, input().split())

# Output
print(count_subsequences(n, m))
