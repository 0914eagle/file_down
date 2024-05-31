
from collections import deque

def min_crossing_time(n, m, islands, g, r):
    MAX_TIME = g + r
    dp = [[-1] * (g + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    queue = deque([(0, 0)])
    while queue:
        pos, time = queue.popleft()

        for i in range(1, m):
            dist = abs(islands[i] - pos)
            t = (time + dist) % MAX_TIME

            if t < g and (dp[islands[i]][g - t] == -1 or dp[islands[i]][g - t] > time + dist):
                dp[islands[i]][g - t] = time + dist
                queue.append((islands[i], time + dist))

        new_pos = pos + 1
        new_time = (time + 1) % MAX_TIME
        if new_pos <= n and dp[new_pos][new_time] == -1:
            dp[new_pos][new_time] = dp[pos][time] + 1
            queue.append((new_pos, new_time))

        new_pos = pos - 1
        if new_pos >= 0 and time % MAX_TIME != 0 and dp[new_pos][time % MAX_TIME] == -1:
            dp[new_pos][time % MAX_TIME] = dp[pos][time] + 1
            queue.append((new_pos, time % MAX_TIME))

    min_time = min(dp[n])
    return min_time if min_time != -1 else -1

n, m = map(int, input().split())
islands = list(map(int, input().split()))
g, r = map(int, input().split())

result = min_crossing_time(n, m, islands, g, r)
print(result)
