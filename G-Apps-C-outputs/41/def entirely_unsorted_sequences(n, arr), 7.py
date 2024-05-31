
MOD = 10**9 + 9

def entirely_unsorted_sequences(n, arr):
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result = (result * i) % MOD
        return result

    sorted_count = {}
    for num in arr:
        if num not in sorted_count:
            sorted_count[num] = 1
        else:
            sorted_count[num] += 1

    total_permutations = factorial(n)
    sorted_permutations = 1

    for count in sorted_count.values():
        sorted_permutations = (sorted_permutations * factorial(count)) % MOD

    unsorted_permutations = total_permutations - sorted_permutations

    return unsorted_permutations % MOD

# Input handling
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(entirely_unsorted_sequences(n, arr))
