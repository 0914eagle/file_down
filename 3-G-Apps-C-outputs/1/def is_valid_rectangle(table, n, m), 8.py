
def is_valid_rectangle(table, n, m):
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                if (i == 0 or table[i-1][j] == 0) and (j == 0 or table[i][j-1] == 0):
                    return False
    return True

def min_cells_to_change(n, m, k, table):
    if k < 0:
        return -1

    if is_valid_rectangle(table, n, m):
        return 0

    count = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                count += 1

    return min(count, k)

n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = min_cells_to_change(n, m, k, table)
print(result)
