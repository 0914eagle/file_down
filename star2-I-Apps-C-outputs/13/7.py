
import sys
import collections

def bfs(grid, start, end, k):
    q = collections.deque([start])
    visited = set([start])
    days = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) == end:
                return days
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] != '#':
                    visited.add((x, y))
                    q.append((x, y))
        days += 1
        if days > k:
            return -1
    return -1

def main():
    n, m, k = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    start = None
    end = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                end = (i, j)
    print(bfs(grid, start, end, k))

if __name__ == "__main__":
    main()

