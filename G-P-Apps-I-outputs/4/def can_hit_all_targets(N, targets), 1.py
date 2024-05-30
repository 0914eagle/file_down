
def can_hit_all_targets(N, targets):
    targets.sort()
    for i in range(N-1):
        x1, y1 = targets[i]
        x2, y2 = targets[i+1]
        dx = x2 - x1
        dy = y2 - y1
        valid = True
        for j in range(N):
            x, y = targets[j]
            if (x - x1) * dy != (y - y1) * dx:
                valid = False
                break
        if valid:
            return "success"
    return "failure"

# Reading input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Calling the function and printing the result
print(can_hit_all_targets(N, targets))
```
