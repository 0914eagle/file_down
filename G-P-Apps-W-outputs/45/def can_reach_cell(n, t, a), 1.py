
def can_reach_cell(n, t, a):
    current_cell = 1
    while current_cell < t:
        current_cell += a[current_cell - 1]
        if current_cell == t:
            return "YES"
    return "NO"

# Input
n, t = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(can_reach_cell(n, t, a))
```
