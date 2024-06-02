
def count_power_of_2_pairs(n, arr):
    count = 0
    powers_of_2 = set([2**i for i in range(31)])  # Pre-calculate powers of 2 up to 2^30
    
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    for i in range(n):
        for j in range(i+1, n):
            total = arr[i] + arr[j]
            if total in powers_of_2:
                count += freq[arr[i]] * freq[arr[j]]
    
    return count // 2  # Divide by 2 to avoid counting pairs twice

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(count_power_of_2_pairs(n, arr))
