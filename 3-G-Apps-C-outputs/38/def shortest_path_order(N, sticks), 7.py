
import heapq

def shortest_path_order(N, sticks):
    def distance_to_edge(x, y):
        return min(x, 10000 - x, y, 10000 - y)

    stick_order = []
    heap = []
    for i, (x1, y1, x2, y2) in enumerate(sticks):
        heapq.heappush(heap, (distance_to_edge(x1, y1), i))
    
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
output = shortest_path_order(N, sticks)
print(' '.join(map(str, output)))
