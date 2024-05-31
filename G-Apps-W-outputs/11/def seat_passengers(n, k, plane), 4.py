
def seat_passengers(n, k, plane):
    def count_neighbors(row, seat_idx):
        neighbors = 0
        for i in range(seat_idx-1, -1, -1):
            if row[i] == 'S':
                neighbors += 1
            else:
                break
        for i in range(seat_idx+1, len(row)):
            if row[i] == 'S':
                neighbors += 1
            else:
                break
        return neighbors
    
    def get_min_neighbors(seats):
        min_neighbors = float('inf')
        for idx, row in enumerate(seats):
            for j, seat in enumerate(row):
                if seat == '.':
                    seats_copy = [list(r) for r in seats]
                    seats_copy[idx][j] = 'P'
                    neighbors = 0
                    for r_idx, r in enumerate(seats_copy):
                        for s_idx, s in enumerate(r):
                            if s == 'S':
                                neighbors += count_neighbors(r, s_idx)
                    if neighbors < min_neighbors:
                        min_neighbors = neighbors
                        best_seat = (idx, j)
        return min_neighbors, best_seat
    
    seats = [list(row) for row in plane]
    
    for _ in range(k):
        _, (best_row, best_seat) = get_min_neighbors(seats)
        seats[best_row][best_seat] = 'P'
    
    total_neighbors = 0
    for row in seats:
        for seat_idx, seat in enumerate(row):
            if seat == 'S':
                total_neighbors += count_neighbors(row, seat_idx)
    
    return total_neighbors, [''.join(row) for row in seats]


# Input
input_data = [
    "4 9",
    "PP.-PPPS-S.S",
    "PSP-PPSP-.S.",
    ".S.-S..P-SS.",
    "P.S-P.PP-PSP"
]

n, k = map(int, input_data[0].split())
plane = input_data[1:]

# Output
total_neighbors, seating_plan = seat_passengers(n, k, plane)
print(total_neighbors)
for row in seating_plan:
    print(row)
