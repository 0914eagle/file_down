
from collections import deque

def solve_crossing_time(n, m, islands, g, r):
    # Initialize distance dictionary with all distances as infinity
    dist = {(i, 0) for i in range(n + 1)}
    
    # Initialize queue for BFS and add starting point to it
    queue = deque([(0, 0)])
    dist[(0, 0)] = 0
    
    while queue:
        curr_pos, curr_time = queue.popleft()
        
        # Calculate time to reach the next point forward or backward
        for new_pos in [curr_pos + 1, curr_pos - 1]:
            if 0 <= new_pos <= n and dist[(new_pos, (curr_time + 1) % (g + r))] == float('inf'):
                dist[(new_pos, (curr_time + 1) % (g + r))] = dist[(curr_pos, curr_time)] + 1
                queue.append((new_pos, (curr_time + 1) % (g + r)))
        
        # Check if changing direction at island is allowed
        for island in islands:
            if curr_pos == island and curr_time < g and dist[(curr_pos, g)] == float('inf'):
                dist[(curr_pos, g)] = dist[(curr_pos, curr_time)]
                queue.append((curr_pos, g))
    
    # Find the minimum time to reach the end point
    min_time = min(dist[(n, i)] for i in range(g))
    
    return min_time if min_time != float('inf') else -1

# Input parsing
n, m = map(int, input().split())
islands = list(map(int, input().split()))
g, r = map(int, input().split())

# Call the function with the provided inputs
output = solve_crossing_time(n, m, islands, g, r)
print(output)
