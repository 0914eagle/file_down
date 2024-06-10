
from collections import deque

def main():
    r, c, k, l = map(int, input().split())
    x0, y0 = map(int, input().split())
    fish_time = [list(map(int, input().split())) for _ in range(r)]
    visited = [[False for _ in range(c)] for _ in range(r)]
    queue = deque([(x0, y0)])
    visited[x0][y0] = True
    max_points = 0
    while queue:
        x, y = queue.popleft()
        if fish_time[x][y] <= l and fish_time[x][y] + k >= 1:
            max_points += 1
        if x - 1 >= 0 and not visited[x - 1][y]:
            queue.append((x - 1, y))
            visited[x - 1][y] = True
        if x + 1 < r and not visited[x + 1][y]:
            queue.append((x + 1, y))
            visited[x + 1][y] = True
        if y - 1 >= 0 and not visited[x][y - 1]:
            queue.append((x, y - 1))
            visited[x][y - 1] = True
        if y + 1 < c and not visited[x][y + 1]:
            queue.append((x, y + 1))
            visited[x][y + 1] = True
    print(max_points)


if __name__ == "__main__":
    main()


