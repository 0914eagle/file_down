
n, m = map(int, input().split())
table = [input() for _ in range(n)]

good_rows = sorted(table, key=lambda s: s)
if good_rows == table:
    print(0)
else:
    count = 0
    for j in range(m):
        column = [row[j] for row in table]
        good_column = sorted(column)
        if good_column != column:
            count += 1
    print(count)

