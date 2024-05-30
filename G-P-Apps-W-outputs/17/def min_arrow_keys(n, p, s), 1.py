
def min_arrow_keys(n, p, s):
    p -= 1  # Convert 1-based indexing to 0-based indexing
    moves = 0
    for i in range(n // 2):
        left_steps = (p - i + n) % n
        right_steps = (i - p + n) % n
        moves += min(left_steps, right_steps)
        moves += min(abs(ord(s[p - i]) - ord(s[p + i])), 26 - abs(ord(s[p - i]) - ord(s[p + i])))
    
    return moves

# Input parsing
n, p = map(int, input().split())
s = input().strip()

print(min_arrow_keys(n, p, s))
```
