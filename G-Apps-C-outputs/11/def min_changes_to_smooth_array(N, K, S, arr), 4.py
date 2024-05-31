
def min_changes_to_smooth_array(N, K, S, arr):
    min_changes = float('inf')

    for i in range(S+1):
        changes = 0
        for j in range(N):
            target = (i + j) % (S+1)
            diff = abs(arr[j] - target)
            changes += min(diff, S-diff)
        
        min_changes = min(min_changes, changes)

    return min_changes

# Read input
N, K, S = map(int, input().split())
arr = [int(x) for x in input().split()]

# Call the function and print the result
result = min_changes_to_smooth_array(N, K, S, arr)
print(result)
