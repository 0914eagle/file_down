
def max_time_to_use_devices(n, p, devices):
    total_power = sum([device[1] for device in devices])
    
    if all([device[0] <= p for device in devices]):
        return -1
    
    time_left = 0
    
    while True:
        min_power = float('inf')
        for device in devices:
            if device[1] < min_power:
                min_power = device[1]
        
        time_to_empty = (min_power - total_power) / sum([device[0] - p for device in devices])
        if time_to_empty <= 0:
            return time_left
        
        time_left += time_to_empty
        for i, device in enumerate(devices):
            devices[i] = (device[0], max(0, device[1] - (time_to_empty * (device[0] - p)))
        
n, p = map(int, input().split())
devices = []
for _ in range(n):
    a, b = map(int, input().split())
    devices.append((a, b))

result = max_time_to_use_devices(n, p, devices)
print("{:.10f}".format(result))
