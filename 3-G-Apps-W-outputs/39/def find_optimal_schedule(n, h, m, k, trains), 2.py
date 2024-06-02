
def find_optimal_schedule(n, h, m, k, trains):
    def check_schedule(t):
        schedule = []
        for i in range(2 * h):
            tram_time = (t + (i * (m // 2))) % m
            schedule.append(tram_time)
        
        for i in range(n):
            train_time = (trains[i][0] * m + trains[i][1]) % (h * m)
            for j in range(2 * h):
                if schedule[j] >= k and schedule[j] - k <= train_time <= schedule[j]:
                    return False
        return True
    
    def cancel_trains(t):
        schedule = []
        for i in range(2 * h):
            tram_time = (t + (i * (m // 2))) % m
            schedule.append(tram_time)
        
        canceled_trains = []
        for i in range(n):
            train_time = (trains[i][0] * m + trains[i][1]) % (h * m)
            can_depart = False
            for j in range(2 * h):
                if schedule[j] >= k and schedule[j] - k <= train_time <= schedule[j]:
                    can_depart = True
                    break
            if not can_depart:
                canceled_trains.append(i + 1)
        
        return canceled_trains
    
    min_canceled = n
    optimal_t = 0
    
    for t in range(m // 2):
        if check_schedule(t):
            canceled_trains = cancel_trains(t)
            if len(canceled_trains) < min_canceled:
                min_canceled = len(canceled_trains)
                optimal_t = t
    
    print(min_canceled, optimal_t)
    if min_canceled > 0:
        print(*cancel_trains(optimal_t))

# Input parsing
n, h, m, k = map(int, input().split())
trains = [list(map(int, input().split())) for _ in range(n)]

find_optimal_schedule(n, h, m, k, trains)
