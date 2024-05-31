
def max_usage_time(n, p, devices):
    total_power = sum([b for a, b in devices])
    min_time = min([(total_power - b) / a for a, b in devices])
    
    if p >= min([a for a, b in devices]):
        return -1
    
    return min_time

# Read input
n, p = map(int, input().split())
devices = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the result
result = max_usage_time(n, p, devices)
print("{:.10f}".format(result))
