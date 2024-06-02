
def count_pairs(n, arr):
    count = 0
    powers_of_two = set([2**i for i in range(31)])  # Generate a set of powers of 2 up to 2^30

    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for i in range(n):
        for j in range(i+1, n):
            total = arr[i] + arr[j]
            if total in powers_of_two:
                count += 1

    for num in freq:
        if 2*num in powers_of_two:
            count += freq[num] * (freq[num] - 1) // 2

    return count

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(count_pairs(n, arr))
