
def count_pairs(n, arr):
    count = 0
    freq = {}
    for num in arr:
        for i in range(32):
            complement = (1 << i) - num
            if complement in freq:
                count += freq[complement]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(count_pairs(n, arr))
