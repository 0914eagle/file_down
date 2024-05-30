
def min_moves_to_equal_strings(s, t):
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    return len(s) + len(t) - 2 * common_length

# Read input
s = input().strip()
t = input().strip()

# Calculate and output result
result = min_moves_to_equal_strings(s, t)
print(result)
```
