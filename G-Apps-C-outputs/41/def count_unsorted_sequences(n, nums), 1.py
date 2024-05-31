
def count_unsorted_sequences(n, nums):
    MOD = 10**9 + 9

    # Count occurrences of each number
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Initialize result with combinations of n elements taken n at a time
    result = 1
    for i in range(n, 0, -1):
        result = (result * i) % MOD

    # Subtract combinations of counts of each number taken count at a time
    for count in counts.values():
        for i in range(count, 0, -1):
            result = (result - (result // i)) % MOD

    return result

# Input reading
n = int(input())
nums = list(map(int, input().split()))

# Output
print(count_unsorted_sequences(n, nums))
