
from collections import deque

def find_minimum_time(n, m, islands, g, r):
    dp = [[-1] * (g + 1) for _ in range(n + 1)]

    dp[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        pos, mod = queue.popleft()

        for d in [-1, 1]:
            new_pos = pos + d
            new_mod = (mod + d) % (g + r)

            if 0 <= new_pos <= n and islands[new_pos] and new_pos != pos:
                new_mod = 0

            if 0 <= new_pos <= n and dp[new_pos][new_mod] == -1:
                dp[new_pos][new_mod] = dp[pos][mod] + 1
                queue.append((new_pos, new_mod))

        if mod < g:
            new_pos = pos
            new_mod = mod + 1

            if 0 <= new_pos <= n and islands[new_pos] and new_pos != pos:
                new_mod = 0

            if 0 <= new_pos <= n and dp[new_pos][new_mod] == -1:
                dp[new_pos][new_mod] = dp[pos][mod] + 1
                queue.append((new_pos, new_mod))

    min_time = min(dp[n])
    return min_time if min_time != -1 else -1

# Input parsing
n, m = map(int, input().split())
islands = [False] * (n + 1)
for island in map(int, input().split()):
    islands[island] = True
g, r = map(int, input().split())

# Output the result
print(find_minimum_time(n, m, islands, g, r))
