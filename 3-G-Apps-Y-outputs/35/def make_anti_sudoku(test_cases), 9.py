
def make_anti_sudoku(test_cases):
    for sudoku in test_cases:
        for i in range(9):
            for j in range(9):
                if i % 3 == j % 3:
                    print((int(sudoku[i][j]) % 9) + 1, end='')
                else:
                    print(sudoku[i][j], end='')
            print()

# Input
t = int(input())
test_cases = []
for _ in range(t):
    sudoku = [input() for _ in range(9)]
    test_cases.append(sudoku)

# Output
make_anti_sudoku(test_cases)
