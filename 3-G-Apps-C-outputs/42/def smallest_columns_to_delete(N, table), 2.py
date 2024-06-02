
def smallest_columns_to_delete(N, table):
    first_row = table[0]
    second_row = table[1]
    third_row = table[2]

    sorted_rows = [sorted(first_row), sorted(second_row), sorted(third_row)]

    count = 0
    for i in range(N):
        if sorted_rows[0][i] != sorted_rows[1][i] or sorted_rows[1][i] != sorted_rows[2][i]:
            count += 1

    return count

# Read input
N = int(input())
table = []
for _ in range(3):
    row = list(map(int, input().split()))
    table.append(row)

# Call the function and output the result
result = smallest_columns_to_delete(N, table)
print(result)
