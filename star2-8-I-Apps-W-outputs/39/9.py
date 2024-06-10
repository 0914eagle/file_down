
n, s = map(int, input().split())
top_floor = s
passenger_list = []
for _ in range(n):
    f, t = map(int, input().split())
    passenger_list.append((t, f))
passenger_list.sort()
current_floor = top_floor
total_time = 0
for arrival_time, floor in passenger_list:
    total_time += abs(current_floor - floor)
    current_floor = floor
print(total_time)

