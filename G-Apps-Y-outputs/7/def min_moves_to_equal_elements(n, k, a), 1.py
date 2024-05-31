
import heapq

def min_moves_to_equal_elements(n, k, a):
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    heap = []
    for key, value in freq.items():
        heapq.heappush(heap, (-value, key))
    
    moves = 0
    while len(heap) > k:
        count, num = heapq.heappop(heap)
        moves += abs(count)
    
    return moves

# Input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_moves_to_equal_elements(n, k, a))
