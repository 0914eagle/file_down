
grid = [input().strip() for _ in range(3)]
diagonal = [grid[i][i] for i in range(3)]
print(''.join(diagonal))
```
