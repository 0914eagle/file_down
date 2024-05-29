
import math

def minimum_time_to_excursion(n, l, v1, v2, k):
    remaining_pupils = n
    total_time = 0
    
    while remaining_pupils > 0:
        # Calculate time taken for all pupils to walk the distance
        time_walk = l / v1
        
        # Determine how many pupils can take the bus
        pupils_in_bus = min(k, remaining_pupils)
        
        # Calculate time taken for the bus to cover the remaining distance
        time_bus = l / v2
        
        # Update the total time and remaining pupils
        total_time += max(time_walk, time_bus)
        remaining_pupils -= pupils_in_bus
        
        # Update the remaining distance for the next iteration
        l -= v1 * time_walk
        
    return total_time

# Read input values
n, l, v1, v2, k = map(int, input().split())

# Call the function and print the output with specified precision
result = minimum_time_to_excursion(n, l, v1, v2, k)
print(f"{result:.10f}")
