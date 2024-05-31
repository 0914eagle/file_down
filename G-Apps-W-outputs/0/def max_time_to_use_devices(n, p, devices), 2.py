
def max_time_to_use_devices(n, p, devices):
    total_power = sum(dev[1] for dev in devices)
    max_time = float('inf')

    for a, b in devices:
        time_to_empty = b / a
        if time_to_empty < max_time:
            max_time = time_to_empty

    if total_power <= p * max_time:
        return -1

    return min(max_time, (total_power - p * max_time) / p)

# Input parsing
n, p = map(int, input().split())
devices = []
for _ in range(n):
    a, b = map(int, input().split())
    devices.append((a, b))

result = max_time_to_use_devices(n, p, devices)
print("{:.10f}".format(result))
