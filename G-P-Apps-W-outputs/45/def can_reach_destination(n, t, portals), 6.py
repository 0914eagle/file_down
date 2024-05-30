
def can_reach_destination(n, t, portals):
    current_cell = 1
    while current_cell < t:
        current_cell += portals[current_cell - 1]
        if current_cell == t:
            return "YES"
    return "NO"

# Input
n, t = map(int, input().split())
portals = list(map(int, input().split()))

# Output
print(can_reach_destination(n, t, portals))
```
