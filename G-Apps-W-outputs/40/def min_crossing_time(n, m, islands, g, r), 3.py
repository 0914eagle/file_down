
from collections import deque

def min_crossing_time(n, m, islands, g, r):
    max_time = g + r
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(max_time)]
    queue = deque([(0, 0, 0)])  # (position, time, direction)
    visited[0][0][0] = True

    while queue:
        pos, curr_time, direction = queue.popleft()

        if pos == n:
            return curr_time

        for i in range(m):
            time_to_next_island = abs(islands[i] - pos)
            time_to_finish = n - pos

            if direction == 0:  # moving to the right
                next_time = curr_time + time_to_next_island
                next_pos = islands[i]
                next_direction = 1
            else:  # moving to the left
                next_time = curr_time + time_to_next_island + g
                next_pos = islands[i]
                next_direction = 0

            if next_time < max_time and not visited[next_time][i][next_direction] and next_time + time_to_finish < max_time:
                visited[next_time][i][next_direction] = True
                queue.append((next_pos, next_time, next_direction))

    return -1

# Input
n, m = map(int, input().split())
islands = list(map(int, input().split()))
g, r = map(int, input().split())

# Output
print(min_crossing_time(n, m, islands, g, r))
