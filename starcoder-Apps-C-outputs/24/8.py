
n = int(input())
grid = []
for i in range(n):
    grid.append(input())

row_evil_count = [0] * n
column_evil_count = [0] * n

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'E':
            row_evil_count[i] += 1
            column_evil_count[j] += 1

evil_count = 0
for i in range(n):
    evil_count += row_evil_count[i]
    evil_count += column_evil_count[i]

if evil_count == 0:
    print("0")
else:
    print("-1")
