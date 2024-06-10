
import sys
from collections import deque

R, C = map(int, input().split())
maze = [input() for _ in range(R)]
joe = None
for r in range(R):
    for c in range(C):
        if maze[r][c] == "J":
            joe = (r, c)
            break
    if joe:
        break

q = deque([(joe, 0)])
visited = {joe}
while q:
    pos, time = q.popleft()
    r, c = pos
    if r == 0 or r == R - 1 or c == 0 or c == C - 1:
        print(time)
        sys.exit()
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        npos = (r + dr, c + dc)
        if maze[npos[0]][npos[1]] != "#" and npos not in visited:
            q.append((npos, time + 1))
            visited.add(npos)

print("IMPOSSIBLE")

