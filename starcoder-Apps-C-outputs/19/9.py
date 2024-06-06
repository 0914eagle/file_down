
from itertools import permutations

data = open("input.txt").read().split('\n')
start_time = data[0]
end_time = data[1]

time_set = list(permutations(end_time, len(end_time)))

for _ in time_set:
    print(start_time)
    start_time = start_time[0] + str(int(start_time[1]) + 1) + start_time[2:]
    if start_time == end_time:
        print(start_time)
        break
