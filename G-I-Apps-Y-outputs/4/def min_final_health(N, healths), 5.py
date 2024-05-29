
import heapq

def min_final_health(N, healths):
    max_heap = [(-health, i) for i, health in enumerate(healths)]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        health1, i = heapq.heappop(max_heap)
        health2, j = heapq.heappop(max_heap)
        
        remaining_health = health1 - health2
        if remaining_health > 0:
            heapq.heappush(max_heap, (remaining_health, i))
    
    return -max_heap[0][0]

# Input processing
N = int(input())
healths = list(map(int, input().split()))

# Calling the function and printing the result
print(min_final_health(N, healths))
```
