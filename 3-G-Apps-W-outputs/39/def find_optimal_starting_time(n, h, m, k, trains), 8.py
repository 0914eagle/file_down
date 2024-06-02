
def find_optimal_starting_time(n, h, m, k, trains):
    def can_depart(tram_time, train_time):
        return abs(tram_time - train_time) >= k

    def cancel_trains(trains, canceled_trains):
        for i in range(len(trains)):
            if i not in canceled_trains:
                print(i+1)

    canceled_trains = set()
    for t in range(m//2):
        valid = True
        for i in range(n):
            if not can_depart(t, trains[i]):
                valid = False
                break
        if valid:
            print(len(canceled_trains), t)
            cancel_trains(trains, canceled_trains)
            return
        else:
            canceled_trains.add((t + k) % (m//2))

n, h, m, k = map(int, input().split())
trains = []
for _ in range(n):
    h_i, m_i = map(int, input().split())
    trains.append(h_i * m + m_i)

find_optimal_starting_time(n, h, m, k, trains)
