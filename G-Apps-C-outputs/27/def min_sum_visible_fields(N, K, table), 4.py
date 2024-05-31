
def min_sum_visible_fields(N, K, table):
    visible_fields = 0
    for row in table:
        visible_fields += sum(row)

    for i in range(N):
        for j in range(N-1):
            horizontal = table[i][j] + table[i][j+1]
            if K > 0:
                visible_fields -= max(horizontal, table[i][j], table[i][j+1])
                K -= 1

    for j in range(N):
        for i in range(N-1):
            vertical = table[i][j] + table[i+1][j]
            if K > 0:
                visible_fields -= max(vertical, table[i][j], table[i+1][j])
                K -= 1

    return visible_fields

# Input processing
input_data = input().split()
N = int(input_data[0])
K = int(input_data[1])
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

# Output the result
print(min_sum_visible_fields(N, K, table))
