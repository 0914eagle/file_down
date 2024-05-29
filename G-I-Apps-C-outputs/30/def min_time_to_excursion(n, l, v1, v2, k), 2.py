
import math

def min_time_to_excursion(n, l, v1, v2, k):
    time_to_walk = l / v1
    trips_needed = math.ceil(n / k)
    time_to_bus = l / v2
    return max(time_to_walk, time_to_bus * trips_needed)

# Input parsing
n, l, v1, v2, k = map(int, input().split())

result = min_time_to_excursion(n, l, v1, v2, k)
print("{:.10f}".format(result))
```
