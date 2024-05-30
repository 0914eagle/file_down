
def valid_move(grid, visited, row, col):
    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and not visited[row][col]:
        return True
    return False

def is_safe(grid, visited, row, col):
    if not visited[row][col]:
        count = 0
        if valid_move(grid, visited, row-1, col):
            count += 1
        if valid_move(grid, visited, row+1, col):
            count += 1
        if valid_move(grid, visited, row, col-1):
            count += 1
        if valid_move(grid, visited, row, col+1):
            count += 1
        return count >= 2
    return False

def find_tour(grid):
    N = len(grid)
    M = len(grid[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    row_moves = [2, 2, -2, -2, 1, 1, -1, -1]
    col_moves = [1, -1, 1, -1, 2, -2, 2, -2]
    row = 0
    col = 0
    visited[row][col] = True
    res = [(row+1, col+1)]

    for i in range(N*M-1):
        next_row = -1
        next_col = -1
        for j in range(8):
            next_row = row + row_moves[j]
            next_col = col + col_moves[j]
            if valid_move(grid, visited, next_row, next_col) and is_safe(grid, visited, next_row, next_col):
                visited[next_row][next_col] = True
                res.append((next_row+1, next_col+1))
                row = next_row
                col = next_col
                break
        if next_row == -1 or next_col == -1:
            return -1

    if is_safe(grid, visited, res[-1][0]-1, res[-1][1]-1) and (abs(res[-1][0]-1 - res[0][0]) + abs(res[-1][1]-1 - res[0][1])) == 2:
        return res
    else:
        return -1

N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
result = find_tour(grid)

if result == -1:
    print(-1)
else:
    for row, col in result:
        print(row, col)
```
