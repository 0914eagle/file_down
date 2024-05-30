
def min_moves_to_equal(s, t):
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    return len(s) + len(t) - 2 * i

# Input
s = input()
t = input()

# Output
print(min_moves_to_equal(s, t))
