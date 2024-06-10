
import sys
import math
import heapq
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(m):
        a, b, w = map(int, input().split())
        edges[a].append((b, w))
        edges[b].append((a, w))
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        distances = [math.inf for _ in range(n + 1)]
        distances[s] = 0
        queue = [(0, s)]
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, edge_weight in edges[current_node]:
                new_distance = current_distance | edge_weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))
        print(distances[t])

if __name__ == '__main__':
    main()

