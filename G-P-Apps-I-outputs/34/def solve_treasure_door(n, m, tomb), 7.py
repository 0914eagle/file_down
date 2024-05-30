
def solve_treasure_door(n, m, tomb):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def can_reach_gargoyle(x, y):
        visited = [[False for _ in range(m)] for _ in range(n)]
        stack = [(x, y)]
        visited[x][y] = True

        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny) and not visited[nx][ny] and tomb[nx][ny] != '#':
                    if tomb[nx][ny] in ['V', 'H']:
                        return True
                    visited[nx][ny] = True
                    stack.append((nx, ny))

        return False

    def rotate_gargoyle(x, y, tomb):
        if tomb[x][y] == 'V':
            tomb[x][y] = 'H'
        else:
            tomb[x][y] = 'V'

    rotated_gargoyles = 0
    for i in range(n):
        for j in range(m):
            if tomb[i][j] in ['V', 'H']:
                if not can_reach_gargoyle(i, j):
                    return -1
                if tomb[i][j] == 'V':
                    rotate_gargoyle(i, j, tomb)
                    rotated_gargoyles += 1
                if not can_reach_gargoyle(i, j):
                    return -1

    return rotated_gargoyles

# Input parsing
n, m = map(int, input().strip().split())
tomb = [list(input().strip()) for _ in range(n)]

result = solve_treasure_door(n, m, tomb)
print(result)
```
