
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

    def count_subsequences_single_element(m):
        return (power(2, m) - 1) % MOD

    result = (power(m, n) - count_subsequences_single_element(m)) % MOD
    return result

# Input
n, m = map(int, input().split())

# Output
print(count_subsequences(n, m))
