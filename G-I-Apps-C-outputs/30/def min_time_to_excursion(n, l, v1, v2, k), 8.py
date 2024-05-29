
import math

def min_time_to_excursion(n, l, v1, v2, k):
    time_to_walk = l / v1
    full_trips = n // k
    remaining_pupils = n % k

    if remaining_pupils == 0:
        total_time = max(time_to_walk, full_trips * l / v2)
    else:
        total_time = max(time_to_walk, (full_trips * (k-1) + remaining_pupils) * l / v2)

    return total_time

# Input parsing
n, l, v1, v2, k = map(int, input().split())

result = min_time_to_excursion(n, l, v1, v2, k)
print("{:.10f}".format(result))
```
