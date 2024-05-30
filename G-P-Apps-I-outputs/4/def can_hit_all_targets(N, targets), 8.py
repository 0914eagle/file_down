
def can_hit_all_targets(N, targets):
    targets.sort()
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = targets[i]
            x2, y2 = targets[j]
            dx = x2 - x1
            dy = y2 - y1
            valid = True
            for k in range(N):
                if k == i or k == j:
                    continue
                x, y = targets[k]
                if dx * (y - y1) != dy * (x - x1):
                    valid = False
                    break
            if valid:
                return "success"
    return "failure"

# Input processing
N = int(input())
targets = []
for _ in range(N):
    x, y = map(int, input().split())
    targets.append((x, y))

# Call the function with input data
result = can_hit_all_targets(N, targets)
print(result)
```
