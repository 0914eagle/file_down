
def minimize_neighbors(n, k, seats):
    status_seats = []
    normal_seats = []
    
    for row in seats:
        for i, seat in enumerate(row):
            if seat == 'S':
                status_seats.append((len(status_seats), i))
            elif seat == 'P':
                normal_seats.append((len(normal_seats), i))

    status_seats.sort(key=lambda x: x[1])
    
    neighbors_sum = 0
    for i in range(len(status_seats)):
        if i > 0 and status_seats[i][1] == status_seats[i-1][1] + 1:
            neighbors_sum += 1

    if k > 0:
        for i in range(k):
            if i % 2 == 0:
                row_idx = normal_seats[i][0]
                seat_idx = status_seats[i][1] - 1
            else:
                row_idx = normal_seats[i][0]
                seat_idx = status_seats[i][1]

            seats[row_idx] = seats[row_idx][:seat_idx] + 'x' + seats[row_idx][seat_idx + 1:]

    return neighbors_sum, seats


# Input parsing
n, k = map(int, input().split())
seats = []
for _ in range(n):
    seats.append(input())

# Solve the problem
result_sum, result_seats = minimize_neighbors(n, k, seats)

# Output the result
print(result_sum)
for row in result_seats:
    print(row)
