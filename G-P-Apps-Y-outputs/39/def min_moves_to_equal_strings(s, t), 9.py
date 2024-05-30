
def min_moves_to_equal_strings(s, t):
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    return len(s) + len(t) - 2 * i

# Read input
s = input().strip()
t = input().strip()

# Output the result
print(min_moves_to_equal_strings(s, t))
```
