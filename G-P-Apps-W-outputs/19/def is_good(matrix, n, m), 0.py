
def is_good(matrix, n, m):
    def count_ones(sub_matrix):
        return sum(row.count('1') for row in sub_matrix)
    
    def is_odd(num):
        return num % 2 != 0
    
    def is_even_length_square(r1, r2, c1, c2):
        return (r2 - r1) == (c2 - c1) and (r2 - r1 + 1) % 2 == 0
    
    def is_good_submatrix(r1, r2, c1, c2):
        ones_count = count_ones([row[c1-1:c2] for row in matrix[r1-1:r2]])
        return is_even_length_square(r1, r2, c1, c2) and is_odd(ones_count)
    
    changes_required = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i, n + 1):
                for l in range(j, m + 1):
                    if not is_good_submatrix(i, k, j, l):
                        changes_required += 1
    
    return changes_required if changes_required > 0 else -1

# Reading input
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Output
print(is_good(matrix, n, m))
