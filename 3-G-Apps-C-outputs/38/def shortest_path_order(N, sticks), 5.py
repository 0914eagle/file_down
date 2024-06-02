
import heapq

def shortest_path_order(N, sticks):
    heap = []
    for i, (x1, y1, x2, y2) in enumerate(sticks):
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        heapq.heappush(heap, (min(y1, y2), i+1))

    return ' '.join(str(heapq.heappop(heap)[1]) for _ in range(N))

# Input parsing
N = int(input())
sticks = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the output
print(shortest_path_order(N, sticks))
