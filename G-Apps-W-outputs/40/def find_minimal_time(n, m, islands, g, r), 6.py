
from collections import deque

def find_minimal_time(n, m, islands, g, r):
    # Initialize the minimum time for each position and each state (position, time, direction)
    dp = [[-1] * (g + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # Create a queue to store the states to be processed
    queue = deque()
    queue.append((0, 0, 0))  # (position, time, direction)

    while queue:
        pos, time, direction = queue.popleft()

        # Calculate the time needed to reach the next position
        next_time = dp[pos][time] + 1

        # Check if Denis can move to the left
        if pos > 0 and next_time <= g and (dp[pos - 1][next_time] == -1 or dp[pos - 1][next_time] > dp[pos][time] + 1):
            if (pos - 1 in islands) or (direction == -1):
                dp[pos - 1][next_time] = dp[pos][time] + 1
                queue.append((pos - 1, next_time, -1))

        # Check if Denis can move to the right
        if pos < n and next_time <= g and (dp[pos + 1][next_time] == -1 or dp[pos + 1][next_time] > dp[pos][time] + 1):
            if (pos + 1 in islands) or (direction == 1):
                dp[pos + 1][next_time] = dp[pos][time] + 1
                queue.append((pos + 1, next_time, 1))

        # Check if Denis can wait for the red light
        if next_time > g:
            # Calculate the time to wait for the next green light
            wait_time = (g + r) - time
            if (dp[pos][wait_time] == -1 or dp[pos][wait_time] > dp[pos][time]):
                dp[pos][wait_time] = dp[pos][time]
                queue.append((pos, wait_time, 0))

    # Find the minimum time to reach the end of the road
    min_time = min(dp[n])
    return min_time if min_time != -1 else -1

# Input parsing
n, m = map(int, input().split())
islands = set(map(int, input().split()))
g, r = map(int, input().split())

# Call the function and output the result
print(find_minimal_time(n, m, islands, g, r))
