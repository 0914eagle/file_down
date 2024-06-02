
def count_subsequences(n, m):
    MOD = 10**9 + 7

    def power(x, y):
        result = 1
        while y > 0:
            if y % 2 == 1:
                result = (result * x) % MOD
            y //= 2
            x = (x * x) % MOD
        return result

    result = power(m, n)
    for i in range(1, m):
        result = (result + power(m - i, n) * power(i, n)) % MOD

    return result

n, m = map(int, input().split())
print(count_subsequences(n, m))
