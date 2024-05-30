
def min_arrow_presses(n, p, s):
    p -= 1
    total_presses = 0

    for i in range(n // 2):
        left_presses = (p - i + n) % n
        right_presses = (i - p + n) % n
        min_presses = min(left_presses, right_presses)

        diff = abs(ord(s[i]) - ord(s[n - 1 - i]))
        total_presses += min_presses + diff

    return total_presses

# Input
n, p = map(int, input().split())
s = input()

# Output
print(min_arrow_presses(n, p, s))
```
