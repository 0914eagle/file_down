
def solve_treasure_door(n, m, tomb):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    mirrors = {'/': ((0, -1), (-1, 0), (0, 1), (1, 0)), '\\': ((0, 1), (1, 0), (0, -1), (-1, 0))}
    
    def bfs(start, dir):
        visited = set()
        queue = [(start, dir)]
        while queue:
            (x, y), dir = queue.pop(0)
            dx, dy = dirs[dir]
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m or tomb[nx][ny] == '#':
                return False
            if tomb[nx][ny] == '.':
                continue
            if (nx, ny) in visited:
                return True
            visited.add((nx, ny))
            if tomb[nx][ny] in mirrors:
                ndir = mirrors[tomb[nx][ny]][dir]
                queue.append(((nx, ny), ndir))
            else:
                return True
        return False

    gargoyle_count = 0
    for i in range(n):
        for j in range(m):
            if tomb[i][j] == 'V':
                for k in range(4):
                    if bfs((i, j), k):
                        break
                else:
                    return -1
            elif tomb[i][j] == 'H':
                for k in range(4):
                    if bfs((i, j), k):
                        break
                else:
                    return -1
                gargoyle_count += 1

    return gargoyle_count

# Input processing
n, m = map(int, input().split())
tomb = []
for _ in range(n):
    row = input().strip()
    tomb.append(row)

# Call the function and output the result
result = solve_treasure_door(n, m, tomb)
print(result)
```
