
def count_unsorted_sequences(n, arr):
    mod = 10**9 + 9
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    sorted_count = 0
    unsorted_count = 0

    for num in freq:
        sorted_count += fact[freq[num]]
        unsorted_count += fact[freq[num] - 1]

    total_unsorted = (fact[n] - sorted_count + unsorted_count) % mod
    return total_unsorted

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the result
result = count_unsorted_sequences(n, arr)
print(result)
