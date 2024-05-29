
import math

def min_time_to_excursion(n, l, v1, v2, k):
    time_on_foot = l / v1
    full_trips = math.ceil(n / k)
    time_on_bus = l / v2
    total_time = max(time_on_foot, time_on_bus * full_trips)
    return total_time

# Input parsing
n, l, v1, v2, k = map(int, input().split())

# Calculate and output the minimum time
print("{:.10f}".format(min_time_to_excursion(n, l, v1, v2, k)))
```
