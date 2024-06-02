
def make_anti_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != '1':
                grid[i] = grid[i][:j] + '1' + grid[i][j+1:]
                break
    return grid

t = int(input())
for _ in range(t):
    sudoku = [input() for _ in range(9)]
    anti_sudoku = make_anti_sudoku(sudoku)
    for row in anti_sudoku:
        print(row)
