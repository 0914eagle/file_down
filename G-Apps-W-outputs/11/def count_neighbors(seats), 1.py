
def count_neighbors(seats):
    neighbors = 0
    for i in range(len(seats)):
        if seats[i] == 'S':
            if i > 0 and seats[i-1] == 'S':
                neighbors += 1
            if i < len(seats) - 1 and seats[i+1] == 'S':
                neighbors += 1
    return neighbors

def minimize_neighbors(n, k, plane):
    rows = plane.split('-')
    status_seats = []
    for row in rows:
        status_seats.extend([seat for seat in row if seat == 'S'])
    
    total_neighbors = count_neighbors(status_seats)
    min_neighbors = total_neighbors
    
    best_plan = plane
    for i in range(len(plane)):
        if plane[i] == '.':
            new_plane = plane[:i] + 'x' + plane[i+1:]
            new_neighbors = minimize_neighbors(n, k-1, new_plane)
            if new_neighbors < min_neighbors:
                min_neighbors = new_neighbors
                best_plan = new_plane

    if k == 0:
        return total_neighbors
    else:
        return min_neighbors

n, k = map(int, input().split())
plane = input()
result = minimize_neighbors(n, k, plane)
print(result)
