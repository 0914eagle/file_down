
def can_use_devices_indefinitely(n, p, devices):
    total_power = sum(b for _, b in devices)
    max_time = float('inf')
    
    for a, b in devices:
        if a > p:
            time_to_empty = b / (a - p)
            max_time = min(max_time, time_to_empty)
    
    if max_time == float('inf'):
        return -1
    else:
        return max_time

# Read input
n, p = map(int, input().split())
devices = [tuple(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = can_use_devices_indefinitely(n, p, devices)
print('{:.10f}'.format(result))
