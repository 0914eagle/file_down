
n, s = map(int, input().split())
passengers = []
for i in range(n):
    floor, time = map(int, input().split())
    passengers.append((floor, time))

passengers.sort(key=lambda x: x[1])

current_floor = s
current_time = 0
total_time = 0

for floor, time in passengers:
    if current_time < time:
        current_time = time
    time_to_floor = current_floor - floor
    time_to_floor = max(time_to_floor, 0)
    current_time += time_to_floor + 1
    current_floor = floor
    total_time = max(total_time, current_time)

print(total_time)

