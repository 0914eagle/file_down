
def min_changes_to_make_substring(S, T):
    min_changes = float('inf')
    for i in range(len(S) - len(T) + 1):
        changes = sum(1 for j in range(len(T)) if S[i+j] != T[j])
        min_changes = min(min_changes, changes)
    return min_changes

# Input
S = input().strip()
T = input().strip()

# Output
print(min_changes_to_make_substring(S, T))
