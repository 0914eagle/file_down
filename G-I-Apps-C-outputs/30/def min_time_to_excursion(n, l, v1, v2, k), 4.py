
import math

def min_time_to_excursion(n, l, v1, v2, k):
    time_to_walk = l / v1
    full_trips = math.ceil(n / k)
    time_for_full_trips = l / v2
    time_for_partial_trip = (l * (full_trips - 1) + min(l, (n % k) * v1)) / v2
    total_time = max(time_to_walk, time_for_full_trips, time_for_partial_trip)
    return "{:.10f}".format(total_time)

# Reading input
n, l, v1, v2, k = map(int, input().split())

# Output the result
print(min_time_to_excursion(n, l, v1, v2, k))
