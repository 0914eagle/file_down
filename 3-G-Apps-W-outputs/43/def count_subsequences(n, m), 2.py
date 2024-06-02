
def count_subsequences(n, m):
    MOD = 10**9 + 7

    def power(x, y):
        res = 1
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % MOD
            x = (x * x) % MOD
            y //= 2
        return res

    def count_subsequences_single(m):
        return (power(2, m) - 1) % MOD

    result = count_subsequences_single(m)
    result = power(result, n)
    print(result)

# Input processing
n, m = map(int, input().split())
count_subsequences(n, m)
