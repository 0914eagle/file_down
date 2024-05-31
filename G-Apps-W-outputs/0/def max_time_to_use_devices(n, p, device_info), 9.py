
def max_time_to_use_devices(n, p, device_info):
    # Sort devices by the ratio of power usage to initial power
    devices_sorted = sorted([(a, b) for a, b in device_info], key=lambda x: x[0] / x[1])

    max_time = float('inf')
    total_power = sum(b for a, b in devices_sorted)
    remaining_power = total_power

    for a, b in devices_sorted:
        if a * total_power <= b * p:
            max_time = -1
            break
        time_needed = (a * remaining_power - b) / p
        if time_needed < max_time:
            max_time = time_needed
        remaining_power -= b

    return max_time

# Read input
n, p = map(int, input().split())
device_info = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
result = max_time_to_use_devices(n, p, device_info)
print("{:.10f}".format(result))
