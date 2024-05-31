
from collections import deque

def min_crossing_time(n, m, islands, g, r):
    dp = [[-1 for _ in range(g)] for _ in range(n + 1)]
    dp[0][0] = 0

    queue = deque([(0, 0)])
    while queue:
        pos, mod = queue.popleft()

        # Check if it's possible to reach the end position
        if pos == n:
            return dp[pos][mod]

        # Move forward
        np = pos + 1
        if np <= n and dp[np][(mod + 1) % g] == -1:
            dp[np][(mod + 1) % g] = dp[pos][mod] + 1
            queue.append((np, (mod + 1) % g))

        # Move backward
        np = pos - 1
        if pos > 0 and (pos in islands) and dp[np][(mod + 1) % g] == -1:
            dp[np][(mod + 1) % g] = dp[pos][mod] + 1
            queue.append((np, (mod + 1) % g))

        # Wait at the same position
        if dp[pos][(mod + 1) % g] == -1:
            dp[pos][(mod + 1) % g] = dp[pos][mod] + 1
            queue.append((pos, (mod + 1) % g))

        # Check if it's possible to change direction on an island
        for island in islands:
            if pos != island and ((pos < island and pos + 1 == island) or (pos > island and pos - 1 == island)):
                np = island
                if dp[np][(mod + 1) % g] == -1:
                    dp[np][(mod + 1) % g] = dp[pos][mod] + 1
                    queue.append((np, (mod + 1) % g))

    return -1

# Read input
n, m = map(int, input().split())
islands = list(map(int, input().split()))
g, r = map(int, input().split())

# Output the result
print(min_crossing_time(n, m, islands, g, r))
