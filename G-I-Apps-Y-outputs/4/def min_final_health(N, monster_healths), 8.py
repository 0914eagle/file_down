
import heapq

def min_final_health(N, monster_healths):
    heap = []
    for health in monster_healths:
        heapq.heappush(heap, -health)
    
    while len(heap) > 1:
        attacking = -heapq.heappop(heap)
        if heap:
            target = -heapq.heappop(heap)
            if attacking > target:
                heapq.heappush(heap, -(attacking - target))
    
    return -heap[0]

# Reading input
N = int(input())
monster_healths = list(map(int, input().split()))

# Calling the function and printing the result
print(min_final_health(N, monster_healths))
```
