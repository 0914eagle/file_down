
def solve_tomb_puzzle(n, m, floorplan):
    def is_valid_position(x, y):
        return 0 <= x < n and 0 <= y < m

    def find_gargoyle_neighbors(x, y):
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while is_valid_position(nx, ny):
                if floorplan[nx][ny] in ['V', 'H']:
                    neighbors.append((nx, ny))
                    break
                if floorplan[nx][ny] == '#' or floorplan[nx][ny] in ['/', '\\']:
                    break
                nx += dx
                ny += dy
        return neighbors

    def is_face_to_face(gargoyle1, gargoyle2):
        x1, y1 = gargoyle1
        x2, y2 = gargoyle2
        return (floorplan[x1][y1] == 'V' and floorplan[x2][y2] == 'V') or (floorplan[x1][y1] == 'H' and floorplan[x2][y2] == 'H')

    def rotate_gargoyle(x, y):
        if floorplan[x][y] == 'V':
            floorplan[x][y] = 'H'
        else:
            floorplan[x][y] = 'V'

    def solve():
        count_rotations = 0
        for i in range(n):
            for j in range(m):
                if floorplan[i][j] in ['V', 'H']:
                    neighbors = find_gargoyle_neighbors(i, j)
                    if len(neighbors) == 0:
                        return -1
                    if not any(is_face_to_face((i, j), neighbor) for neighbor in neighbors):
                        rotate_gargoyle(i, j)
                        count_rotations += 1
        return count_rotations

    return solve()

# Input parsing
n, m = map(int, input().split())
floorplan = [list(input()) for _ in range(n)]

result = solve_tomb_puzzle(n, m, floorplan)
print(result)
```
