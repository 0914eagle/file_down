
def min_moves_to_equal_strings(s, t):
    n = len(s)
    m = len(t)
    i, j = 0, 0
    while i < n and j < m and s[n-1-i] == t[m-1-j]:
        i += 1
        j += 1
    return n + m - 2*i

# Reading input
s = input().strip()
t = input().strip()

# Output minimum number of moves
print(min_moves_to_equal_strings(s, t))
```
