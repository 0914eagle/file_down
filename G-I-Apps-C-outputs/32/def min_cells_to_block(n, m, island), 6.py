
def min_cells_to_block(n, m, island):
    row_max = [0] * n
    col_max = [0] * m

    for i in range(n):
        for j in range(m):
            if island[i][j] == '#':
                row_max[i] = max(row_max[i], j)
                col_max[j] = max(col_max[j], i)

    blocked_cells = 0
    for i in range(n):
        for j in range(m):
            if i < col_max[j] and j < row_max[i]:
                blocked_cells += 1

    return blocked_cells

# Input parsing
n, m = map(int, input().split())
island = [input() for _ in range(n)]

# Call the function and print the output
print(min_cells_to_block(n, m, island))
