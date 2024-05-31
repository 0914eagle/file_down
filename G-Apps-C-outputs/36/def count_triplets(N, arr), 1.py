
def count_triplets(N, arr):
    count = 0
    freq = {}
    
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] in freq:
                count += freq[arr[i] + arr[j]]
            if arr[i] + arr[j] not in freq:
                freq[arr[i] + arr[j]] = 0
            freq[arr[i] + arr[j]] += 1
            
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(count_triplets(N, arr))
