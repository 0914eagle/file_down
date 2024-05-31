
def min_changes_to_smooth_array(N, K, S, array):
    changes = 0

    for i in range(N):
        total = sum(array[i:i+K])
        expected_sum = S * K
        changes += abs(total - expected_sum)

    return changes

# Read input
N, K, S = map(int, input().split())
array = [int(x) for x in input().split()]

# Output the result
print(min_changes_to_smooth_array(N, K, S, array))
