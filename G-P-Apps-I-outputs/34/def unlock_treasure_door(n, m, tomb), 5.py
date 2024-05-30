
def unlock_treasure_door(n, m, tomb):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(x, y, dx, dy):
        while is_valid(x, y) and tomb[x][y] != '#':
            if tomb[x][y] in mirror_map:
                dx, dy = mirror_map[tomb[x][y]][dx][dy]
            if tomb[x][y] in gargoyle_map:
                gargoyle_map[tomb[x][y]] += 1
            x, y = x + dx, y + dy

    mirror_map = {'/': {(-1, 0): (0, 1), (1, 0): (0, -1), (0, 1): (-1, 0), (0, -1): (1, 0)},
                  '\\': {(-1, 0): (0, -1), (1, 0): (0, 1), (0, 1): (1, 0), (0, -1): (-1, 0)}}

    gargoyle_map = {'V': 0, 'H': 0}

    for i in range(n):
        for j in range(m):
            if tomb[i][j] in gargoyle_map:
                if gargoyle_map[tomb[i][j]] == 0:
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        dfs(i + dx, j + dy, dx, dy)

    if gargoyle_map['V'] % 2 == 0 and gargoyle_map['H'] % 2 == 0:
        return (gargoyle_map['V'] + gargoyle_map['H']) // 2
    else:
        return -1

# Input parsing
n, m = map(int, input().split())
tomb = [input() for _ in range(n)]

# Call the function and output the result
print(unlock_treasure_door(n, m, tomb))
```

