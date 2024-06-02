
def solve_freight_trains(n, h, m, k, trains):
    def can_depart(tram_time, train_time):
        return abs((tram_time - train_time) % (h * m)) >= k

    canceled_trains = []
    for i in range(n):
        for j in range(i+1, n):
            if not can_depart(trains[i], trains[j]) or not can_depart(trains[j], trains[i]):
                canceled_trains.append(i+1)
                break

    min_canceled = len(canceled_trains)
    optimal_t = 0

    for t in range(1, m//2):
        canceled_trains_t = []
        for i in range(n):
            if not can_depart(t, trains[i]):
                canceled_trains_t.append(i+1)

        if len(canceled_trains_t) < min_canceled:
            min_canceled = len(canceled_trains_t)
            optimal_t = t
            canceled_trains = canceled_trains_t

    print(min_canceled, optimal_t)
    print(*canceled_trains)

# Input parsing
n, h, m, k = map(int, input().split())
trains = []
for _ in range(n):
    h_i, m_i = map(int, input().split())
    trains.append(h_i * m + m_i)

solve_freight_trains(n, h, m, k, trains)
