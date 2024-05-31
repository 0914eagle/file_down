
def minimize_neighbors(n, k, seats):
    status_seats = set()
    free_seats = []

    for row in seats:
        for i, seat in enumerate(row):
            if seat == 'S':
                status_seats.add((len(free_seats), i))
            elif seat == '.':
                free_seats.append((len(free_seats), i))

    min_neighbors = float('inf')
    best_plan = []

    for i in range(len(free_seats)):
        for j in range(i+1, len(free_seats)):
            plan = seats.copy()
            plan[free_seats[i][0]] = plan[free_seats[i][0]][:free_seats[i][1]] + 'P' + plan[free_seats[i][0]][free_seats[i][1]+1:]
            plan[free_seats[j][0]] = plan[free_seats[j][0]][:free_seats[j][1]] + 'P' + plan[free_seats[j][0]][free_seats[j][1]+1:]
            
            neighbors = 0
            for row, col in status_seats:
                if col-1 >= 0 and plan[row][col-1] == 'P':
                    neighbors += 1
                if col+1 < len(plan[row]) and plan[row][col+1] == 'P':
                    neighbors += 1

            if neighbors < min_neighbors:
                min_neighbors = neighbors
                best_plan = plan

    return min_neighbors, best_plan


n, k = map(int, input().split())
seats = [input() for _ in range(n)]

min_neighbors, best_plan = minimize_neighbors(n, k, seats)

print(min_neighbors)
for row in best_plan:
    print(row)
