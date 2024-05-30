
def min_moves_to_equal_strings(s, t):
    i = 0
    while i < len(s) and i < len(t) and s[i] == t[i]:
        i += 1
    return len(s) + len(t) - 2*i

s = input().strip()
t = input().strip()

print(min_moves_to_equal_strings(s, t))
```
