
def solve_treasure_door(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def rotate_gargoyle(x, y):
        nonlocal rotated_gargoyles
        if tomb[x][y] == 'V':
            rotated_gargoyles.add((x, y))
            for dx, dy in [(0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and tomb[nx][ny] != '#' and (nx, ny) not in rotated_gargoyles:
                    rotate_gargoyle(nx, ny)
        elif tomb[x][y] == 'H':
            rotated_gargoyles.add((x, y))
            for dx, dy in [(1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and tomb[nx][ny] != '#' and (nx, ny) not in rotated_gargoyles:
                    rotate_gargoyle(nx, ny)

    rotated_gargoyles = set()
    for i in range(n):
        for j in range(m):
            if tomb[i][j] in ['V', 'H'] and (i, j) not in rotated_gargoyles:
                rotate_gargoyle(i, j)

    for i in range(n):
        for j in range(m):
            if tomb[i][j] in ['V', 'H'] and (i, j) not in rotated_gargoyles:
                return -1

    return len(rotated_gargoyles)

# Input
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Output
print(solve_treasure_door(n, m, tomb))
```
