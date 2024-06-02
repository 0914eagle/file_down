
def min_changes_to_make_substring(s, t):
    min_changes = float('inf')
    for i in range(len(s) - len(t) + 1):
        changes = sum(s[i+j] != t[j] for j in range(len(t)))
        min_changes = min(min_changes, changes)
    return min_changes

# Read input
s = input().strip()
t = input().strip()

# Calculate and print the minimum number of changes needed
print(min_changes_to_make_substring(s, t))
