
def find_min_cells_to_change(n, m, k, table):
    def is_valid_rectangle(start_row, end_row, start_col, end_col):
        ones_count = 0
        zeros_count = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if table[i][j] == 1:
                    ones_count += 1
                else:
                    zeros_count += 1
        return ones_count == (end_row - start_row + 1) * (end_col - start_col + 1) or zeros_count == (end_row - start_row + 1) * (end_col - start_col + 1)

    def count_cells_in_rectangle(start_row, end_row, start_col, end_col):
        return (end_row - start_row + 1) * (end_col - start_col + 1)

    def get_min_cells_to_change():
        min_cells_to_change = float('inf')
        for start_row in range(n):
            for end_row in range(start_row, n):
                for start_col in range(m):
                    for end_col in range(start_col, m):
                        if is_valid_rectangle(start_row, end_row, start_col, end_col):
                            cells_to_change = count_cells_in_rectangle(start_row, end_row, start_col, end_col)
                            ones_count = 0
                            for i in range(start_row, end_row + 1):
                                for j in range(start_col, end_col + 1):
                                    if table[i][j] == 1:
                                        ones_count += 1
                            zeros_count = cells_to_change - ones_count
                            if ones_count <= k and zeros_count <= k:
                                min_cells_to_change = min(min_cells_to_change, cells_to_change - ones_count)
        return min_cells_to_change if min_cells_to_change != float('inf') else -1

    return get_min_cells_to_change()

# Input parsing
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = find_min_cells_to_change(n, m, k, table)
print(result)
