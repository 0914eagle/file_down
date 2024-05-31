
def min_changes_to_smooth_array(N, K, S, arr):
    min_changes = float('inf')
    
    for smooth_val in range(S+1):
        changes = 0
        for i in range(N):
            diff = abs(arr[i] - smooth_val)
            changes += min(diff, S-diff)
            if i >= K:
                prev_val = arr[i-K]
                diff = abs(prev_val - smooth_val)
                changes -= min(diff, S-diff)
            if i >= K-1:
                min_changes = min(min_changes, changes)
    
    return min_changes

# Read input
N, K, S = map(int, input().split())
arr = [int(x) for x in input().split()]

# Call the function
result = min_changes_to_smooth_array(N, K, S, arr)
print(result)
