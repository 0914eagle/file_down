
def min_changes(S, T):
    min_changes = float('inf')
    for i in range(len(S) - len(T) + 1):
        changes = sum([1 for j in range(len(T)) if S[i+j] != T[j]])
        min_changes = min(min_changes, changes)
    return min_changes

# Read input from Standard Input
S = input().strip()
T = input().strip()

# Call the function and print the result
print(min_changes(S, T))
