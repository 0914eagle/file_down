
import heapq

def shortest_path_order(N, sticks):
    events = []
    for i, (x1, y1, x2, y2) in enumerate(sticks):
        events.append((min(x1, x2), i, 1))
        events.append((max(x1, x2), i, -1))
    
    events.sort()
    
    heap = []
    result = []
    for _, i, direction in events:
        if direction == 1:
            heapq.heappush(heap, i)
        else:
            result.append(heapq.heappop(heap) + 1)
    
    return result

# Input
N = 4
sticks = [(1, 3, 2, 2), (1, 1, 3, 2), (2, 4, 7, 3), (3, 3, 5, 3)]

# Output
print(*shortest_path_order(N, sticks))
