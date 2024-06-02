
def min_columns_to_delete(N, table):
    rows = [sorted(row) for row in table]
    count = 0
    for i in range(N):
        if rows[0][i] != rows[1][i] or rows[0][i] != rows[2][i]:
            count += 1
    return count

# Read input
N = int(input())
table = [list(map(int, input().split())) for _ in range(3)]

# Call the function and output the result
result = min_columns_to_delete(N, table)
print(result)
