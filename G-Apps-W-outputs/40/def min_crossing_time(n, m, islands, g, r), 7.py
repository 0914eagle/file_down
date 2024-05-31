
from collections import deque

def min_crossing_time(n, m, islands, g, r):
    # Initialize the visited set to keep track of visited positions and directions
    visited = set()
    
    # Initialize the deque for BFS containing tuples of (position, time_passed, is_green_light_on)
    queue = deque([(0, 0, True)])
    
    while queue:
        position, time_passed, is_green_light_on = queue.popleft()
        
        if position == n:
            return time_passed
        
        # If the current position and state have been visited before, skip
        if (position, is_green_light_on) in visited:
            continue
        
        visited.add((position, is_green_light_on))
        
        # Calculate the next positions and times based on current state
        if is_green_light_on:
            for next_pos in [-1, 1]:
                new_pos = position + next_pos
                
                if 0 <= new_pos <= n and new_pos not in islands:
                    queue.append((new_pos, time_passed + 1, True))
        else:
            queue.append((position, time_passed + 1, True))
            
        if position in islands and not is_green_light_on:
            queue.append((position, time_passed + 1, False))
            
            if position != 0:
                queue.extend([(position, time_passed + 1, False) for _ in range(g - time_passed)])
    
    return -1

# Input parsing
n, m = map(int, input().split())
islands = set(map(int, input().split()))
g, r = map(int, input().split())

print(min_crossing_time(n, m, islands, g, r))
