
def min_changes_to_make_smooth_array(N, K, S, arr):
    min_changes = 0
    for i in range(N - K + 1):
        target_sum = S * K
        current_sum = sum(arr[i:i+K])
        changes = abs(target_sum - current_sum)
        min_changes = max(min_changes, changes)
    return min_changes

# Read input
N, K, S = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Calculate and output the result
result = min_changes_to_make_smooth_array(N, K, S, arr)
print(result)
