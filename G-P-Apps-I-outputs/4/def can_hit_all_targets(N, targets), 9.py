
def can_hit_all_targets(N, targets):
    targets.sort()
    for i in range(N-1):
        x1, y1 = targets[i]
        x2, y2 = targets[i+1]
        dx, dy = x2 - x1, y2 - y1
        line_targets = [targets[i]]
        for j in range(i+1, N):
            x3, y3 = targets[j]
            if dx*(y3-y1) == dy*(x3-x1):
                line_targets.append(targets[j])
        if len(line_targets) == N:
            return "success"
    return "failure"

# Reading input
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Calling the function
result = can_hit_all_targets(N, targets)
print(result)
```
