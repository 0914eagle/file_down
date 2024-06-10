
n, s = map(int, input().split())
times = [0] * (s + 1)
for _ in range(n):
    f, t = map(int, input().split())
    times[f] = t

current_floor = s
total_time = 0
for floor in range(s, 0, -1):
    if times[floor] == 0:
        continue
    time_to_wait = times[floor] - total_time
    if time_to_wait > 0:
        total_time += time_to_wait
    total_time += floor - current_floor
    current_floor = floor

print(total_time)

