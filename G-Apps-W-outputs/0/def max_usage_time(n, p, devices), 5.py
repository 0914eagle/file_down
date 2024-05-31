
def max_usage_time(n, p, devices):
    total_power = sum([device[1] for device in devices])
    min_power = min([device[1] / device[0] for device in devices])
    
    if min_power >= p:
        return -1
    
    time = 0
    while True:
        required_power = sum([device[0] * time - device[1] for device in devices if device[0] * time > device[1]])
        if required_power > total_power + p * time:
            return time
        time += 1

# Read input
n, p = map(int, input().split())
devices = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = max_usage_time(n, p, devices)
print("{:.10f}".format(result))
