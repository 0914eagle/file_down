
def max_device_usage_time(n, p, devices):
    total_power = sum([device[1] for device in devices])
    min_power = min([device[1] / device[0] for device in devices])
    
    if total_power >= p * min_power:
        return -1
    
    left = 0
    right = 10**15
    
    while right - left > 1e-6:
        mid = (left + right) / 2
        charge_time = 0
        
        for device in devices:
            if mid * device[0] > device[1]:
                charge_time += (mid * device[0] - device[1]) / p
        
        if charge_time <= mid:
            right = mid
        else:
            left = mid
    
    return left

# Input parsing
n, p = map(int, input().split())
devices = [list(map(int, input().split())) for _ in range(n)]

result = max_device_usage_time(n, p, devices)
print("{:.10f}".format(result))
