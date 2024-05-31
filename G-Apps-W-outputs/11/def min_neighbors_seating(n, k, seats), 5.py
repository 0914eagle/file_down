
def min_neighbors_seating(n, k, seats):
    status_passengers = []
    for row in seats:
        status_passengers += [i for i, seat in enumerate(row) if seat == 'S']

    status_passengers.sort()
    total_neighbors = sum(abs(status_passengers[i] - status_passengers[i+1]) - 1 for i in range(len(status_passengers) - 1))

    additional_passengers = k
    i = 0
    while additional_passengers > 0:
        if i >= len(status_passengers) - 1:
            break
        neighbors = abs(status_passengers[i] - status_passengers[i+1]) - 1
        if neighbors == 0:
            i += 1
            continue
        if additional_passengers >= neighbors:
            for j in range(1, neighbors + 1):
                seats[status_passengers[i] + j] = 'x'
            additional_passengers -= neighbors
        else:
            for j in range(1, additional_passengers + 1):
                seats[status_passengers[i] + j] = 'x'
            additional_passengers = 0
        i += 1

    new_status_passengers = [i for i, seat in enumerate(seats) if seat == 'S']
    new_status_passengers.sort()
    new_total_neighbors = sum(abs(new_status_passengers[i] - new_status_passengers[i+1]) - 1 for i in range(len(new_status_passengers) - 1))
    
    return new_total_neighbors, seats

# Input parsing
n, k = map(int, input().split())
seats = []
for _ in range(n):
    seats.extend(list(input()))

result_neighbors, result_seating = min_neighbors_seating(n, k, seats)

# Output
print(result_neighbors)
for i in range(0, len(result_seating), 3):
    print(''.join(result_seating[i:i+3]))
