
def sum_of_table_cells(n, rectangles):
    table = [[0 for _ in range(100)] for _ in range(100)]
    
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        for i in range(y1-1, y2):
            for j in range(x1-1, x2):
                table[i][j] += 1
    
    total_sum = sum(sum(row) for row in table)
    return total_sum

# Input
n = 2
rectangles = [(1, 1, 2, 3), (2, 2, 3, 3)]

# Output
print(sum_of_table_cells(n, rectangles))
