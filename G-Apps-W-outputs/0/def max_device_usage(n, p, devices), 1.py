
def max_device_usage(n, p, devices):
    total_power = sum([device[1] for device in devices])
    max_time = float('inf')

    for i in range(n):
        device_power, device_storage = devices[i]
        if device_power > p:
            time = device_storage / (device_power - p)
            max_time = min(max_time, time)

    if max_time == float('inf'):
        return -1
    else:
        return max_time

# Input processing
n, p = map(int, input().split())
devices = []
for _ in range(n):
    a, b = map(int, input().split())
    devices.append((a, b))

# Output
result = max_device_usage(n, p, devices)
print(f"{result:.10f}")
