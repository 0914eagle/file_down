
import heapq

def min_vertical_moves(n, m, malls):
    vertical_moves = 0
    remaining_items = set(range(1, m+1))
    vertical_distance = []
    
    for i in range(1, m+1):
        vertical_distance.append([])
        
    for x, y, t in malls:
        vertical_distance[t-1].append(abs(x) - abs(y))
    
    for distances in vertical_distance:
        distances.sort()
    
    for distances in vertical_distance:
        for d in distances:
            if len(remaining_items) == 0:
                break
            vertical_moves += 1
            remaining_items.remove(d)
    
    return vertical_moves - 1

# Reading input
n, m = map(int, input().split())
malls = [list(map(int, input().split())) for _ in range(n)]

# Calling the function
result = min_vertical_moves(n, m, malls)

# Printing the result
print(result)
```
