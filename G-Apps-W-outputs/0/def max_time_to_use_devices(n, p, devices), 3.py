
def max_time_to_use_devices(n, p, devices):
    total_power = sum([device[1] for device in devices])
    time = 0
    while True:
        min_power = min([device[1] + device[0] * time for device in devices])
        if min_power >= total_power:
            return -1
        max_charge_time = min([(total_power - min_power) / p, min([(device[1] + device[0] * time) / p for device in devices if device[0] * time > device[1]])])
        time += max_charge_time
        for i in range(n):
            devices[i][1] += devices[i][0] * max_charge_time
    return time

# Input parsing
n, p = map(int, input().split())
devices = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output with the required precision
result = max_time_to_use_devices(n, p, devices)
print("{:.10f}".format(result))
