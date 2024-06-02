
def count_subsequences(n, m):
    MOD = 10**9 + 7

    def power(base, exp):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % MOD
            base = (base * base) % MOD
            exp //= 2
        return result

    def count_subsequences_single_element(m):
        return power(2, m) - 1

    result = count_subsequences_single_element(m)
    result = power(result, n)
    print(result)

# Input
n, m = map(int, input().split())
count_subsequences(n, m)
