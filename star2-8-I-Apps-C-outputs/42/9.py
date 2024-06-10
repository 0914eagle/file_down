
import sys
from collections import deque


def solve(maze):
    queue = deque()
    visited = set()
    R, C = len(maze), len(maze[0])

    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'J':
                queue.append((r, c, 0))
                visited.add((r, c))

    while queue:
        r, c, time = queue.popleft()
        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            return time
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C and maze[r + dr][c + dc] != '#' and (r + dr, c + dc) not in visited:
                queue.append((r + dr, c + dc, time + 1))
                visited.add((r + dr, c + dc))
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split())
    maze = []
    for _ in range(R):
        maze.append(sys.stdin.readline().rstrip())
    print(solve(maze))

