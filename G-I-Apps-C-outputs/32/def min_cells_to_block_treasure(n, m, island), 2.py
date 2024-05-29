
def min_cells_to_block_treasure(n, m, island):
    if n == 1 or m == 1:
        return 0
    
    reachable = [[False for _ in range(m)] for _ in range(n)]
    reachable[0][0] = True
    
    for i in range(n):
        for j in range(m):
            if island[i][j] == '#':
                continue
            if i > 0 and reachable[i-1][j]:
                reachable[i][j] = True
            if j > 0 and reachable[i][j-1]:
                reachable[i][j] = True
    
    if reachable[n-1][m-1]:
        return 0
    
    blocked_cells = 0
    i, j = n-1, m-1
    while i > 0 or j > 0:
        if i > 0 and j > 0 and not reachable[i-1][j] and not reachable[i][j-1]:
            blocked_cells += 1
            i, j = i-1, j-1
        elif i > 0 and reachable[i-1][j]:
            i -= 1
        elif j > 0 and reachable[i][j-1]:
            j -= 1
    
    return blocked_cells

# Input parsing
n, m = map(int, input().split())
island = [input() for _ in range(n)]

result = min_cells_to_block_treasure(n, m, island)
print(result)
```
