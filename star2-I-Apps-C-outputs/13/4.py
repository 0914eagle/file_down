
import sys

def solve(grid, stamina):
    n, m = len(grid), len(grid[0])
    start_pos = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start_pos = (i, j)
                break
        if start_pos is not None:
            break
    if start_pos is None:
        print("Invalid input: no starting point")
        sys.exit(1)
    queue = [start_pos]
    visited = [[False] * m for _ in range(n)]
    visited[start_pos[0]][start_pos[1]] = True
    days = 0
    while queue:
        next_queue = []
        for i, j in queue:
            if grid[i][j] == 'G':
                return days
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y] != '#':
                    next_queue.append((x, y))
                    visited[x][y] = True
        queue = next_queue
        days += 1
    return -1

def main():
    n, m, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    print(solve(grid, k))

if __name__ == '__main__':
    main()

