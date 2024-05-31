
def count_triplets(N, arr):
    count = 0
    
    # Count occurrences of each number in the array
    num_count = {}
    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    # Find all possible combinations of i, j, k
    for i in range(N):
        for j in range(i+1, N):
            k = arr[i] + arr[j]
            if k in num_count:
                count += num_count[k]
                # Exclude the case where i, j, and k are the same number
                if k == arr[i] and k == arr[j]:
                    count -= 2
    
    return count

# Read input
N = int(input())
arr = list(map(int, input().split()))

# Call the function and print the result
print(count_triplets(N, arr))
