
def count_pairs(n, arr):
    count = 0
    powers_of_two = set([2**i for i in range(31)])  # Pre-calculate powers of 2 up to 2^30
    
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for i in range(n):
        for j in range(i+1, n):
            total = arr[i] + arr[j]
            if total in powers_of_two:
                count += freq[arr[i]] * freq[arr[j]]
    
    return count

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(count_pairs(n, arr))
