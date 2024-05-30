
def can_reach_cell(n, t, portals):
    current_cell = 1
    while current_cell < t:
        current_cell += portals[current_cell - 1]
        if current_cell == t:
            return "YES"
    return "NO"

n, t = map(int, input().split())
portals = list(map(int, input().split()))
result = can_reach_cell(n, t, portals)
print(result)
```
