
def can_hit_all_targets(N, targets):
    targets.sort()
    
    if N == 1:
        return "success"
    
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = targets[i]
            x2, y2 = targets[j]
            
            dx = x2 - x1
            dy = y2 - y1
            
            seen = set()
            seen.add((x1, y1))
            seen.add((x2, y2))
            
            for k in range(N):
                if k == i or k == j:
                    continue
                
                x, y = targets[k]
                
                if dx == 0:
                    if x == x1:
                        seen.add((x, y))
                else:
                    slope = float(dy) / dx
                    if y - y1 == slope * (x - x1):
                        seen.add((x, y))
            
            if len(seen) == N:
                return "success"
    
    return "failure"

# Read input
N = int(input())
targets = []
for _ in range(N):
    X, Y = map(int, input().split())
    targets.append((X, Y))

# Call the function and print the output
print(can_hit_all_targets(N, targets))
```
