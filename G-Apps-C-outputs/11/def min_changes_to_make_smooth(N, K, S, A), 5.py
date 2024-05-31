
def min_changes_to_make_smooth(N, K, S, A):
    changes = 0
    for i in range(N - K):
        window_sum = sum(A[i:i+K])
        required_sum = S * K
        changes += abs(window_sum - required_sum)
    return changes

# Read input
N, K, S = map(int, input().split())
A = [int(num) for num in input().split()]

# Calculate and print the minimum number of changes
print(min_changes_to_make_smooth(N, K, S, A))
