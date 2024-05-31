
def count_adjacent_bombs(grid, row, col):
    bomb_count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == '#':
            bomb_count += 1
    return bomb_count

def replace_empty_with_bomb_count(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = ''
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                bomb_count = count_adjacent_bombs(grid, i, j)
                new_row += str(bomb_count)
            else:
                new_row += grid[i][j]
        new_grid.append(new_row)
    return new_grid

if __name__ == "__main__":
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    result = replace_empty_with_bomb_count(grid)

    for row in result:
        print(row)
