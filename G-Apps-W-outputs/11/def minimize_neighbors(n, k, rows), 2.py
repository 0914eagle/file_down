
def minimize_neighbors(n, k, rows):
    row_seats = 3 + 4 + 3
    status_seats = 0
    neighbors = 0
    result = []

    for row in rows:
        status_seats += row.count('S')

    for row in rows:
        available_seats = row.count('.')
        if k > 0:
            for i in range(len(row) - row_seats + 1):
                if row[i:i+row_seats].count('.') == k:
                    for j in range(row_seats):
                        if row[i+j] == '.':
                            row = row[:i+j] + 'x' + row[i+j+1:]
                            k -= 1
                    break

        result.append(row)

    for row in result:
        neighbors += row.count('SP') + row.count('PS')

    return neighbors, result

# Input parsing
n, k = map(int, input().split())
rows = []
for _ in range(n):
    row = input().strip()
    rows.append(row)

min_neighbors, result = minimize_neighbors(n, k, rows)
print(min_neighbors)
for row in result:
    print(row)
