
from collections import deque

def wait_time_at_destination(n, m, trails):
    adj_list = [[] for _ in range(n)]
    for u, v, d in trails:
        adj_list[u].append((v, d))
    
    visited_day = [-1] * n
    visited_knight = [-1] * n
    queue = deque([(0, 0, True)])  # (cabin, time, is_day)
    
    while queue:
        curr_cabin, curr_time, is_day = queue.popleft()
        if is_day:
            visited_day[curr_cabin] = curr_time
        else:
            visited_knight[curr_cabin] = curr_time
        
        for next_cabin, duration in adj_list[curr_cabin]:
            next_time = curr_time + duration
            if is_day and next_time <= 12:
                if visited_day[next_cabin] == -1 or next_time < visited_day[next_cabin]:
                    queue.append((next_cabin, next_time, True))
            else:
                if visited_knight[next_cabin] == -1 or next_time < visited_knight[next_cabin]:
                    queue.append((next_cabin, next_time, False))
    
    return visited_day[n-1] - visited_knight[n-1]

# Sample Input
n, m = 5, 6
trails = [
    (0, 1, 2),
    (0, 3, 8),
    (1, 2, 11),
    (2, 3, 5),
    (2, 4, 2),
    (4, 3, 9)
]

print(wait_time_at_destination(n, m, trails))
```
