
def find_min_neighbors_seating(n, k, rows):
    status_passengers = []
    normal_passengers = []

    for row in rows:
        for seat in row:
            if seat == 'S':
                status_passengers.append('S')
            elif seat == 'P':
                normal_passengers.append('P')

    status_neighbors = 0
    for i in range(len(status_passengers)):
        if i > 0 and status_passengers[i - 1] == 'S':
            status_neighbors += 1
        if status_passengers[i] == 'S' and i < len(status_passengers) - 1 and status_passengers[i + 1] == 'S':
            status_neighbors += 1

    min_neighbors = status_neighbors

    for i in range(k):
        for j in range(n):
            if rows[j][3] == '.':
                rows[j] = rows[j][:3] + 'x' + rows[j][4:]
                k -= 1
                break

    print(min_neighbors)
    for row in rows:
        print(row)

n, k = map(int, input().split())
rows = [input() for _ in range(n)]

find_min_neighbors_seating(n, k, rows)
