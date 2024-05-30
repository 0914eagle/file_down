
def min_arrow_key_presses(n, p, s):
    p -= 1  # Adjust index to 0-based
    left_moves = p
    right_moves = n - 1 - p
    total_moves = min(left_moves, right_moves) + abs(left_moves - right_moves)

    changes = 0
    for i in range(n // 2):
        diff = abs(ord(s[i]) - ord(s[n - 1 - i]))
        changes += min(diff, 26 - diff)

    return total_moves + changes

# Input parsing
n, p = map(int, input().split())
s = input()

# Calculate and output the result
print(min_arrow_key_presses(n, p, s))
```
