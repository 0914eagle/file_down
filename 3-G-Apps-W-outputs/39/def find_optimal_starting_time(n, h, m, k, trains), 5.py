
def find_optimal_starting_time(n, h, m, k, trains):
    def can_depart(tram_time, train_time):
        if tram_time < k:
            return train_time >= tram_time + k
        else:
            return train_time >= tram_time or train_time >= tram_time + k

    def can_schedule(tram_times):
        for i in range(n):
            for j in range(i + 1, n):
                if not can_depart(tram_times[i], trains[j]):
                    return False
        return True

    best_cancelled = n
    best_starting_time = 0
    cancelled_trains = []

    for t in range(m // 2):
        tram_times = [t + (m // 2) * i for i in range(n)]
        cancelled = sum(not can_schedule(tram_times) for _ in range(n))
        if cancelled < best_cancelled:
            best_cancelled = cancelled
            best_starting_time = t
            cancelled_trains = [i + 1 for i in range(n) if not can_schedule(tram_times)]

    return best_cancelled, best_starting_time, cancelled_trains

# Input parsing
n, h, m, k = map(int, input().split())
trains = [tuple(map(int, input().split())) for _ in range(n)]

# Find optimal starting time and cancelled trains
cancelled, starting_time, cancelled_trains = find_optimal_starting_time(n, h, m, k, trains)

# Output results
print(cancelled, starting_time)
print(*cancelled_trains)
