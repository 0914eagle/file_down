
def min_changes_to_make_substring(s, t):
    min_changes = len(t)
    for i in range(len(s) - len(t) + 1):
        changes = sum(1 for j in range(len(t)) if s[i+j] != t[j])
        min_changes = min(min_changes, changes)
    return min_changes

# Read input from Standard Input
s = input().strip()
t = input().strip()

# Output the result
print(min_changes_to_make_substring(s, t))
