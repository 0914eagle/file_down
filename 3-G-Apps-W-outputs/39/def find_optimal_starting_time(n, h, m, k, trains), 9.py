
def find_optimal_starting_time(n, h, m, k, trains):
    canceled_trains = []
    
    for t in range(m//2):
        valid = True
        for i in range(n):
            train_hour = trains[i][0]
            train_minute = trains[i][1]
            tram_minute = (t + k) % m
            if (train_hour == 0 and train_minute >= t and train_minute < t + k) or (train_hour == 0 and tram_minute >= t and tram_minute < t + k):
                valid = False
                break
        
        if valid:
            return 0, t
    
    for i in range(n):
        canceled_trains.append(i+1)
    
    return n, 0, canceled_trains

# Input parsing
n, h, m, k = map(int, input().split())
trains = []
for _ in range(n):
    h_i, m_i = map(int, input().split())
    trains.append((h_i, m_i))

# Find optimal starting time and canceled trains
min_canceled_trains, optimal_starting_time, canceled_trains = find_optimal_starting_time(n, h, m, k, trains)

# Output
print(min_canceled_trains, optimal_starting_time)
if min_canceled_trains > 0:
    print(*canceled_trains)
