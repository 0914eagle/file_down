
def find_optimal_starting_time(n, h, m, k, trains):
    def can_depart(train_time, tram_time, boarding_time):
        if tram_time < boarding_time:
            return train_time <= tram_time or train_time >= tram_time + m - k
        else:
            return train_time <= tram_time < train_time + k

    def cancel_trains(trains, start_time):
        canceled_trains = []
        for i, (train_hour, train_minute) in enumerate(trains):
            train_time = train_hour * m + train_minute
            tram_time = start_time
            boarding_time = tram_time + k
            if not can_depart(train_time, tram_time, boarding_time):
                canceled_trains.append(i + 1)
        return canceled_trains

    min_canceled = n
    optimal_start_time = 0

    for start_time in range(m // 2):
        canceled = cancel_trains(trains, start_time)
        if len(canceled) < min_canceled:
            min_canceled = len(canceled)
            optimal_start_time = start_time

    return min_canceled, optimal_start_time

# Input parsing
n, h, m, k = map(int, input().split())
trains = [list(map(int, input().split())) for _ in range(n)]

# Find optimal starting time and number of canceled trains
min_canceled, optimal_start_time = find_optimal_starting_time(n, h, m, k, trains)

# Output
print(min_canceled, optimal_start_time)
for train in cancel_trains(trains, optimal_start_time):
    print(train)
