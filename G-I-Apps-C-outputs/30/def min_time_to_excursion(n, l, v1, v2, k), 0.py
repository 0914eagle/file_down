
import math

def min_time_to_excursion(n, l, v1, v2, k):
    # Calculate the time it takes for all pupils to walk to the excursion
    time_walk = l / v1
    
    # Calculate the time it takes for the bus to make multiple trips and transport all pupils
    trips = math.ceil(n / k)  # Calculate the number of trips needed
    time_bus = l / (v2 * trips)  # Calculate the time it takes for the bus
    
    return max(time_walk, time_bus)

# Input reading and function call
n, l, v1, v2, k = map(int, input().split())
result = min_time_to_excursion(n, l, v1, v2, k)
print("{:.10f}".format(result))
```
