
def min_columns_to_delete(N, table):
    rows = [sorted(row) for row in table]
    count = 0
    for col in range(N):
        if rows[0][col] != rows[1][col] or rows[0][col] != rows[2][col]:
            count += 1
    return count

# Input processing
N = int(input())
table = [list(map(int, input().split())) for _ in range(3)]

# Call the function and output the result
result = min_columns_to_delete(N, table)
print(result)
