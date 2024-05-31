
def max_time_to_zero_power(n, p, devices):
    total_power = sum(device[1] for device in devices)
    min_time = float('inf')

    for device in devices:
        if device[1] >= total_power - device[0]:
            min_time = min(min_time, (total_power - device[0]) / p / n)

    if min_time == float('inf'):
        return -1
    else:
        return min_time

# Read input
n, p = map(int, input().split())
devices = []
for _ in range(n):
    a, b = map(int, input().split())
    devices.append((a, b))

# Calculate and print output
result = max_time_to_zero_power(n, p, devices)
print("{:.10f}".format(result))
