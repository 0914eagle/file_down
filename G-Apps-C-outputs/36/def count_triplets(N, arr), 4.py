
def count_triplets(N, arr):
    count = 0
    possible_sums = set()
    
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] in possible_sums:
                count += 1
            possible_sums.add(arr[i] + arr[j])
    
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Call function and output result
result = count_triplets(N, arr)
print(result)
