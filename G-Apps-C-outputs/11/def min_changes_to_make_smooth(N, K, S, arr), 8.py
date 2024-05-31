
def min_changes_to_make_smooth(N, K, S, arr):
    min_changes = float('inf')
    
    for i in range(S+1):
        changes = 0
        for j in range(N):
            changes += min(abs(arr[j] - i), S - abs(arr[j] - i))
            if j >= K:
                changes -= min(abs(arr[j-K] - i), S - abs(arr[j-K] - i))
                
            if j >= K - 1:
                min_changes = min(min_changes, changes)
    
    return min_changes

# Reading input
N, K, S = map(int, input().split())
arr = [int(x) for x in input().split()]

# Calling the function and printing the result
result = min_changes_to_make_smooth(N, K, S, arr)
print(result)
