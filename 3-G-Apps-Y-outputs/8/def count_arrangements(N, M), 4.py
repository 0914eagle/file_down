
def count_arrangements(N, M):
    MOD = 10**9 + 7

    # Calculate the factorial of a number modulo MOD
    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact = (fact * i) % MOD
        return fact

    # Calculate the modular inverse of a number
    def mod_inv(n):
        return pow(n, MOD-2, MOD)

    # Calculate the number of arrangements
    total = factorial(N + M)
    dog_arrangements = factorial(N)
    monkey_arrangements = factorial(M)

    # Calculate the number of invalid arrangements where dogs or monkeys are adjacent
    invalid = dog_arrangements * monkey_arrangements % MOD

    # Calculate the number of valid arrangements
    valid = total - invalid

    return valid % MOD

# Read input values
N, M = map(int, input().split())

# Call the function and print the result
print(count_arrangements(N, M))
