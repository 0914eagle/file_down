
from collections import deque

def bfs(maze, start, end):
    m, n = len(maze), len(maze[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = deque([(start, 0)])
    visited[start[0]][start[1]] = True

    while queue:
        curr, curr_dist = queue.popleft()
        if curr == end:
            return curr_dist
        for i, j in [(curr[0] + 1, curr[1]), (curr[0] - 1, curr[1]), (curr[0], curr[1] + 1), (curr[0], curr[1] - 1)]:
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and maze[i][j] != '#':
                queue.append(((i, j), curr_dist + 1))
                visited[i][j] = True

    return -1

def solve(maze):
    m, n = len(maze), len(maze[0])
    start = None
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 'J':
                start = (i, j)
                break
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 'F':
                fire_dist = bfs(maze, (i, j), start)
                if fire_dist != -1:
                    return "IMPOSSIBLE"
    joe_dist = bfs(maze, start, None)
    if joe_dist != -1:
        return joe_dist
    else:
        return "IMPOSSIBLE"

def main():
    r, c = map(int, input().split())
    maze = []
    for _ in range(r):
        maze.append(input())
    print(solve(maze))

main()

