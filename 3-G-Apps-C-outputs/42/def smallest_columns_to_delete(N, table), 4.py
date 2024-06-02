
def smallest_columns_to_delete(N, table):
    rows = [list(map(int, row)) for row in table]
    sorted_rows = [sorted(row) for row in rows]
    
    count = 0
    for i in range(N):
        if sorted_rows[0][i] != sorted_rows[1][i] or sorted_rows[0][i] != sorted_rows[2][i]:
            count += 1
    
    return count

# Read input
N = int(input())
table = [input().split() for _ in range(3)]

# Call the function and output the result
result = smallest_columns_to_delete(N, table)
print(result)
