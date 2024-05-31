
def find_min_neighbors(n, k, seats):
    neighbors = 0
    plan = []
    for row in seats:
        for i in range(len(row) - 6):
            if row[i:i+3] == 'SS.' or row[i:i+3] == '.SS':
                neighbors += 1
            if row[i:i+4] == 'S.S.':
                neighbors += 2
    
    for row in seats:
        new_row = ''
        for i in range(len(row) - 1):
            if row[i] == '.':
                new_row += 'x' if k > 0 else '.'
                k -= 1
            else:
                new_row += row[i]
        plan.append(new_row)
    
    print(neighbors)
    for row in plan:
        print(row)

# Input processing
n, k = map(int, input().split())
seats = []
for _ in range(n):
    seats.append(input())

find_min_neighbors(n, k, seats)
