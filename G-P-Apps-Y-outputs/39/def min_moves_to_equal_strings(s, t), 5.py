
def min_moves_to_equal_strings(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t) and s[i] == t[j]:
        i += 1
        j += 1
    return len(s) + len(t) - 2 * i

# Read input
s = input().strip()
t = input().strip()

# Calculate and output minimum moves
print(min_moves_to_equal_strings(s, t))
