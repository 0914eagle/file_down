
def minimal_sum_visible_fields(N, K, table):
    rows = len(table)
    cols = len(table[0])

    visible_fields = 0
    dominoes = 0

    for i in range(rows):
        for j in range(cols - 1):
            if dominoes < K:
                visible_fields += table[i][j]
                dominoes += 1

    for i in range(cols):
        for j in range(rows - 1):
            if dominoes < K:
                visible_fields += table[j][i]
                dominoes += 1

    return visible_fields

# Input
N, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# Output
print(minimal_sum_visible_fields(N, K, table))
