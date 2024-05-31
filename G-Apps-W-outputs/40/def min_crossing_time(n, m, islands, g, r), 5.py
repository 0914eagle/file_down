
from collections import deque

def min_crossing_time(n, m, islands, g, r):
    distances = [[-1] * (g + 1) for _ in range(n + 1)]
    q = deque([(0, 0, 0)])  # (position, time elapsed, time since last change)

    distances[0][0] = 0

    while q:
        pos, time, time_since_change = q.popleft()

        if pos == n:
            return time

        # Move to the right
        if pos + 1 <= n and distances[pos + 1][(time + 1) % (g + r)] == -1:
            if (time_since_change == 0 and pos + 1 in islands) or time_since_change == g:
                distances[pos + 1][(time + 1) % (g + r)] = time + 1
                q.append((pos + 1, time + 1, 0))
            else:
                distances[pos + 1][(time + 1) % (g + r)] = time + 1
                q.append((pos + 1, time + 1, time_since_change + 1))

        # Move to the left
        if pos - 1 >= 0 and distances[pos - 1][(time + 1) % (g + r)] == -1:
            if (time_since_change == 0 and pos - 1 in islands) or time_since_change == g:
                distances[pos - 1][(time + 1) % (g + r)] = time + 1
                q.append((pos - 1, time + 1, 0))
            else:
                distances[pos - 1][(time + 1) % (g + r)] = time + 1
                q.append((pos - 1, time + 1, time_since_change + 1))

    return -1

# Read input values
n, m = map(int, input().split())
islands = set(map(int, input().split()))
g, r = map(int, input().split())

# Call the function and output the result
result = min_crossing_time(n, m, islands, g, r)
print(result)
