
import math

def min_time_to_excursion(n, l, v1, v2, k):
    time_pupil = l / v1
    
    full_trips = n // k
    remaining_pupils = n % k
    
    if remaining_pupils == 0:
        return max(time_pupil, l / v2)
    
    time_first_bus = l / v2
    time_buses = max(time_pupil, time_first_bus * full_trips + (l - full_trips * k * v2) / ((k + 1) * v2))
    
    return time_buses

# Input parsing
n, l, v1, v2, k = map(int, input().split())

result = min_time_to_excursion(n, l, v1, v2, k)
print("{:.10f}".format(result))
