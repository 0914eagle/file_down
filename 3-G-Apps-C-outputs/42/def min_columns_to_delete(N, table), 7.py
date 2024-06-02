
def min_columns_to_delete(N, table):
    counts = [{}, {}, {}]
    for i in range(N):
        for j in range(3):
            num = table[j][i]
            counts[j][num] = counts[j].get(num, 0) + 1

    delete_count = N
    for i in range(N):
        delete_count = min(delete_count, N - counts[0][table[0][i]] + 1)
    
    return delete_count

# Read input
N = int(input())
table = []
for _ in range(3):
    row = list(map(int, input().split()))
    table.append(row)

# Call the function and output the result
result = min_columns_to_delete(N, table)
print(result)
