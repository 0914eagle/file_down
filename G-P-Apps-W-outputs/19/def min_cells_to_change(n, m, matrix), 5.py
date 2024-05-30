
def min_cells_to_change(n, m, matrix):
    def is_good_submatrix(top_left, bottom_right):
        count_ones = prefix_sum[bottom_right[0]][bottom_right[1]] - prefix_sum[bottom_right[0]][top_left[1]-1] - prefix_sum[top_left[0]-1][bottom_right[1]] + prefix_sum[top_left[0]-1][top_left[1]-1]
        return count_ones % 2 == 1
    
    prefix_sum = [[0] * (m+1) for _ in range(n+1)]
    changes_required = 0
    
    for i in range(n):
        for j in range(m):
            prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + int(matrix[i][j])
    
    for length in range(2, min(n, m)+1, 2):
        for i in range(n-length+1):
            for j in range(m-length+1):
                top_left = (i, j)
                bottom_right = (i+length-1, j+length-1)
                if not is_good_submatrix(top_left, bottom_right):
                    changes_required += 1
    
    return changes_required if changes_required > 0 else -1

# Input processing
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Output
print(min_cells_to_change(n, m, matrix))
