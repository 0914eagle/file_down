
def minimal_sum_visible_fields(N, K, table):
    visible_sum = 0
    for i in range(N):
        for j in range(N):
            visible_sum += table[i][j]

    horizontal_dominoes = [[0] * N for _ in range(N)]
    vertical_dominoes = [[0] * N for _ in range(N)]

    for _ in range(K):
        for i in range(N):
            for j in range(N-1):
                if horizontal_dominoes[i][j] == 0 and horizontal_dominoes[i][j+1] == 0:
                    if table[i][j] + table[i][j+1] > table[i][j] + table[i][j+1]:
                        horizontal_dominoes[i][j] = 1
                        horizontal_dominoes[i][j+1] = 1
                        visible_sum -= max(table[i][j], table[i][j+1])

        for j in range(N):
            for i in range(N-1):
                if vertical_dominoes[i][j] == 0 and vertical_dominoes[i+1][j] == 0:
                    if table[i][j] + table[i+1][j] > table[i][j] + table[i+1][j]:
                        vertical_dominoes[i][j] = 1
                        vertical_dominoes[i+1][j] = 1
                        visible_sum -= max(table[i][j], table[i+1][j])

    return visible_sum

# Read input
N, K = map(int, input().split())
table = []
for _ in range(N):
    row = list(map(int, input().split()))
    table.append(row)

# Call the function and print the result
result = minimal_sum_visible_fields(N, K, table)
print(result)
