
def find_optimal_starting_time(n, h, m, k, trains):
    def can_trains_depart(tram_time, trains, k):
        for train_time in trains:
            if abs(tram_time - train_time) < k:
                return False
        return True

    min_canceled_trains = n
    optimal_starting_time = 0
    canceled_trains = []

    for t in range(m // 2):
        canceled = 0
        for i in range(n):
            if not can_trains_depart(t, trains, k):
                canceled += 1
                break
            t += m // 2
        if canceled < min_canceled_trains:
            min_canceled_trains = canceled
            optimal_starting_time = t % (m // 2)

    for i in range(n):
        if not can_trains_depart(optimal_starting_time, trains, k):
            canceled_trains.append(i + 1)
            trains.remove(trains[0])

    print(min_canceled_trains, optimal_starting_time)
    for train in canceled_trains:
        print(train)

# Input parsing
n, h, m, k = map(int, input().split())
trains = []
for _ in range(n):
    h_i, m_i = map(int, input().split())
    trains.append(h_i * 60 + m_i)

find_optimal_starting_time(n, h, m, k, trains)
