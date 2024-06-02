
def find_optimal_starting_time(n, h, m, k, trains):
    def can_depart(tram_time, train_time):
        return abs(tram_time - train_time) >= k
    
    trains.sort(key=lambda x: (x[0], x[1]))
    
    canceled_trains = []
    for t in range(m // 2):
        valid = True
        for i in range(n):
            if not can_depart(t, trains[i][0] * m + trains[i][1]):
                valid = False
                break
        if valid:
            return 0, t
    
    for i in range(n):
        canceled_trains.append(i+1)
    
    return n, 0, canceled_trains

# Input parsing
n, h, m, k = map(int, input().split())
trains = [list(map(int, input().split())) for _ in range(n)]

# Find optimal starting time and canceled trains
min_canceled, optimal_start, canceled_trains = find_optimal_starting_time(n, h, m, k, trains)

# Output
print(min_canceled, optimal_start)
if min_canceled > 0:
    print(*canceled_trains)
