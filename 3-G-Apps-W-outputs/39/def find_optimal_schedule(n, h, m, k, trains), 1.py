
def find_optimal_schedule(n, h, m, k, trains):
    def can_depart(t):
        last_departure = -k
        for i in range(2 * h):
            if i % 2 == 0:
                last_departure = i * (m // 2) + t
            if any(abs(train - last_departure) < k for train in trains):
                return False
        return True

    best_t = 0
    min_canceled = n
    for t in range(m // 2):
        canceled = sum(abs(train - t) < k or abs(train - (t + m // 2)) < k for train in trains)
        if canceled < min_canceled and can_depart(t):
            min_canceled = canceled
            best_t = t

    canceled_trains = [i + 1 for i, train in enumerate(trains) if abs(train - best_t) < k or abs(train - (best_t + m // 2)) < k]

    return min_canceled, best_t, canceled_trains

# Input
n, h, m, k = map(int, input().split())
trains = [0] * n
for i in range(n):
    h_i, m_i = map(int, input().split())
    trains[i] = h_i * m + m_i

# Output
min_canceled, best_t, canceled_trains = find_optimal_schedule(n, h, m, k, trains)
print(min_canceled, best_t)
for train in canceled_trains:
    print(train)
