mize_neighbors(n, k, seats):
    def count_neighbors(row):
        neighbors = 0
        for i in range(len(row)):
            if row[i] == 'S':
                if i > 0 and row[i-1] == 'S':
                    neighbors += 1
                if i < len(row) - 1 and row[i+1] == 'S':
                    neighbors += 1
        return neighbors

    def update_seats(row, count, k):
        for i in range(len(row)):
            if k == 0:
                break
            if row[i] == '.':
                row[i] = 'x'
                k -= 1
        return row, k

    total_neighbors = 0
    
    for row in seats:
        total_neighbors += count_neighbors(row)

    print(total_neighbors)

    for i in range(n):
        if k == 0:
            break
        seats[i], k = update_seats(seats[i], total_neighbors, k)
    
    for row in seats:
        print(''.join(row))

# Input parsing
n, k = map(int, input().split())
seats = []
for _ in range(n):
    seats.append(list(input()))

minimize_neighbors(n, k, seats)
[/PYTHON