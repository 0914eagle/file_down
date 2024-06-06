
# -*- coding: utf-8 -*-
from operator import itemgetter, attrgetter


class Train:
    def __init__(self, hour, minute, kind):
        self.hour = hour
        self.minute = minute
        self.kind = kind

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minute < other.minute
        return self.hour < other.hour


def solve(num_trains, num_hours, num_minutes, boarding_time, times):
    num_half_hours = num_hours * num_minutes // 2
    trains = []
    for i in range(len(times)):
        trains.append(Train(times[i][0], times[i][1], 1))
    for i in range(num_half_hours):
        trains.append(Train(i // (num_minutes // 2), (i % (num_minutes // 2)) * 2 + 1, 2))
    trains = sorted(trains)
    best = num_trains
    best_t = 0
    for i in range(num_minutes // 2):
        if trains[i].kind == 2:
            trains[i].hour = -1
            trains[i].minute = -1
        cancels = 0
        starts = num_half_hours
        for j in range(num_trains):
            if starts > j:
                starts -= 1
            elif trains[j].kind == 1:
                cancels += 1
        if cancels < best:
            best = cancels
            best_t = i
    print(best, best_t)
    for i in range(best):
        print(i + 1, end=' ')
    print()
    return best


n, h, m, k = map(int, input().split())
times = []
for i in range(n):
    times.append(list(map(int, input().split())))
solve(n, h, m, k, times)

