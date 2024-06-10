
n, s = [int(x) for x in input().split()]
passengers = []
for _ in range(n):
    f, t = [int(x) for x in input().split()]
    passengers.append((t, f))
passengers.sort(key=lambda x: x[0])
current_floor = s
current_time = 0
for t, f in passengers:
    current_time += abs(current_floor - f)
    current_floor = f
print(current_time)

