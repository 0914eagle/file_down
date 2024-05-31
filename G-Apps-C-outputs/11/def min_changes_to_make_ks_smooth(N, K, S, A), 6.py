
def min_changes_to_make_ks_smooth(N, K, S, A):
    def is_ks_smooth(arr):
        for i in range(K - 1, len(arr)):
            if sum(arr[i - K + 1:i + 1]) != S:
                return False
        return True

    min_changes = float('inf')
    for start_val in range(S + 1):
        changes = 0
        for i in range(N):
            if A[i] != (start_val + i % K) % (S + 1):
                changes += 1
        min_changes = min(min_changes, changes)

    return min_changes

# Read input
N, K, S = map(int, input().split())
A = [int(x) for x in input().split()]

# Call the function and print the result
print(min_changes_to_make_ks_smooth(N, K, S, A))
