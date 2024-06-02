
def count_arrangements(N, M):
    MOD = 10**9 + 7

    # Calculate the factorial of a number modulo MOD
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % MOD
        return result

    # Calculate the modular inverse of a number modulo MOD using Fermat's Little Theorem
    def mod_inverse(n):
        return pow(n, MOD - 2, MOD)

    # Calculate the number of arrangements using combinatorial mathematics
    total_animals = N + M
    total_arrangements = factorial(total_animals)

    # Calculate the number of invalid arrangements where dogs or monkeys are adjacent
    invalid_arrangements = factorial(N) * factorial(M) % MOD

    # Calculate the number of valid arrangements
    valid_arrangements = total_arrangements - invalid_arrangements

    return valid_arrangements % MOD

# Read input from Standard Input
N, M = map(int, input().split())

# Print the result
print(count_arrangements(N, M))
