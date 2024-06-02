
def find_optimal_starting_time(n, h, m, k, trains):
    def can_depart(tram_time, train_time):
        return tram_time >= train_time or tram_time + k <= train_time
    
    def count_canceled_trains(start_time):
        canceled_trains = []
        for i in range(n):
            if not can_depart(start_time, trains[i]):
                canceled_trains.append(i+1)
        return len(canceled_trains), canceled_trains
    
    best_start_time = 0
    min_canceled_trains = n
    for t in range(m//2):
        canceled_trains, _ = count_canceled_trains(t)
        if canceled_trains < min_canceled_trains:
            min_canceled_trains = canceled_trains
            best_start_time = t
    
    canceled_trains, canceled_train_list = count_canceled_trains(best_start_time)
    
    print(min_canceled_trains, best_start_time)
    for train in canceled_train_list:
        print(train)

# Input parsing
n, h, m, k = map(int, input().split())
trains = []
for _ in range(n):
    h_i, m_i = map(int, input().split())
    trains.append(h_i * 60 + m_i)

# Call the function with the input values
find_optimal_starting_time(n, h, m, k, trains)
