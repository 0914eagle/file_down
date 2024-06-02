
import heapq

def shortest_path_order(N, sticks):
    sticks_with_index = [(i, x1, y1, x2, y2) for i, (x1, y1, x2, y2) in enumerate(sticks)]
    sticks_with_index.sort(key=lambda x: (min(x[1], x[3]), max(x[1], x[3])))
    
    result = []
    heap = []
    
    for i, x1, y1, x2, y2 in sticks_with_index:
        heapq.heappush(heap, (min(y1, y2), i))
    
    while heap:
        _, i = heapq.heappop(heap)
        result.append(i+1)
        
        new_heap = []
        for j, (x1, y1, x2, y2) in enumerate(sticks):
            if j != i:
                if x1 <= min(sticks[i][0], sticks[i][2]) <= x2 or x1 <= max(sticks[i][0], sticks[i][2]) <= x2:
                    heapq.heappush(new_heap, (min(y1, y2), j))
        heap = new_heap
    
    return result

# Input
N = int(input())
sticks = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    sticks.append((x1, y1, x2, y2))

# Output
result = shortest_path_order(N, sticks)
print(*result)
