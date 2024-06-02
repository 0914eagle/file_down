
import heapq

def shortest_path_order(N, sticks):
    stick_order = []
    heap = []
    
    for i, stick in enumerate(sticks):
        x1, y1, x2, y2 = stick
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        heapq.heappush(heap, (min(y1, y2), i))
    
    while heap:
        _, i = heapq.heappop(heap)
        stick_order.append(i + 1)
    
    return stick_order

# Input processing
N = int(input())
sticks = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    sticks.append((x1, y1, x2, y2))

# Call the function and print the output
result = shortest_path_order(N, sticks)
print(' '.join(map(str, result)))
