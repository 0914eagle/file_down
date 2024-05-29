
def restore_secret_array(t, test_cases):
    for n, x, y in test_cases:
        diff = y - x
        max_element = x + (n - 1) * diff
        arr = [max(1, max_element - (n - 1) * diff) + i * diff for i in range(n)]
        print(*arr)

# Input parsing
t = int(input())
test_cases = []
for _ in range(t):
    n, x, y = map(int, input().split())
    test_cases.append((n, x, y))

# Function call
restore_secret_array(t, test_cases)
```
