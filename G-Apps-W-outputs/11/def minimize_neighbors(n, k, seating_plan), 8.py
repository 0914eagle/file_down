
def minimize_neighbors(n, k, seating_plan):
    def count_neighbors(row):
        neighbors = 0
        for i in range(len(row)-1):
            if row[i] == 'S' and row[i+1] == 'S':
                neighbors += 1
            if row[i] == 'S' and row[i+1] == 'P':
                neighbors += 2
        return neighbors

    def update_seating_plan(row, new_passenger):
        return row.replace('.', new_passenger, 1)

    min_neighbors = float('inf')
    min_seating_plan = ''
    
    for i in range(n):
        row = seating_plan[i]
        for j in range(len(row)):
            if row[j] == '.':
                temp_seating_plan = seating_plan[:i] + [update_seating_plan(row, 'x')] + seating_plan[i+1:]
                temp_neighbors = count_neighbors(temp_seating_plan[i])
                if temp_neighbors < min_neighbors:
                    min_neighbors = temp_neighbors
                    min_seating_plan = temp_seating_plan

    print(min_neighbors)
    for row in min_seating_plan:
        print(row)

# Input
n, k = map(int, input().split())
seating_plan = []
for _ in range(n):
    seating_plan.append(input())

# Solve
minimize_neighbors(n, k, seating_plan)
