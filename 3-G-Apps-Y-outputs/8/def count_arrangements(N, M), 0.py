
def count_arrangements(N, M):
    MOD = 10**9 + 7

    def factorial(n):
        result = 1
        for i in range(1, n+1):
            result = (result * i) % MOD
        return result

    def power(base, exp):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % MOD
            base = (base * base) % MOD
            exp //= 2
        return result

    total = N + M
    if abs(N - M) > 1:
        return 0

    if N == M:
        return (factorial(N) * factorial(M) * 2) % MOD
    else:
        return (factorial(N) * factorial(M)) % MOD

# Read input
N, M = map(int, input().split())

# Calculate and print the result
print(count_arrangements(N, M))
