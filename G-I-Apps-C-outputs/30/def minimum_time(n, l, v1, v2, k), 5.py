
import math

def minimum_time(n, l, v1, v2, k):
    bus_capacity = min(k, n)  # Seats available in the bus
    time_to_reach = l / v1  # Time taken if all pupils walk individually
    total_trips = math.ceil(n / bus_capacity)  # Number of trips needed for all pupils
    time_to_busstop = l / v2  # Time taken to reach bus stop
    time_waiting = (total_trips - 1) * time_to_busstop  # Total waiting time for pupils while taking trips
    total_time = max(time_to_reach, time_waiting + time_to_busstop)
    return total_time

# Input handling
input_values = input().split()
n = int(input_values[0])
l = int(input_values[1])
v1 = int(input_values[2])
v2 = int(input_values[3])
k = int(input_values[4])

result = minimum_time(n, l, v1, v2, k)
print("{:.10f}".format(result))
```
