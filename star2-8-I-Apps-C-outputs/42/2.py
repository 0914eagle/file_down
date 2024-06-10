
import sys
from collections import deque

def solve(maze):
    R, C = len(maze), len(maze[0])
    q = deque()
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'J':
                q.append((r, c, 0))
    visited = set()
    while q:
        r, c, t = q.popleft()
        if r == 0 or r == R-1 or c == 0 or c == C-1:
            return t
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= r+dr < R and 0 <= c+dc < C and maze[r+dr][c+dc] != '#' and (r+dr, c+dc) not in visited:
                q.append((r+dr, c+dc, t+1))
    return "IMPOSSIBLE"

def main():
    R, C = map(int, input().split())
    maze = [input() for _ in range(R)]
    print(solve(maze))

if __name__ == '__main__':
    main()


