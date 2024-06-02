
def count_pairs(n, arr):
    count = 0
    powers_of_two = set([2**i for i in range(31)])
    
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) in powers_of_two:
                count += freq[arr[i]] * freq[arr[j]]
    
    return count // 2

# Input parsing
n = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
result = count_pairs(n, arr)
print(result)
