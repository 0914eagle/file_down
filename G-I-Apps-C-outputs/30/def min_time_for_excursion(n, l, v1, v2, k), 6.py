
import math

def min_time_for_excursion(n, l, v1, v2, k):
    time_to_walk = l / v1
    full_trips = math.ceil(n / k)
    time_to_bus = l / v2
    total_time = max(time_to_walk, full_trips * time_to_bus)
    
    return total_time

# Input parsing
n, l, v1, v2, k = map(int, input().split())

# Call the function and output the result
result = min_time_for_excursion(n, l, v1, v2, k)
print("{:.10f}".format(result))
```
