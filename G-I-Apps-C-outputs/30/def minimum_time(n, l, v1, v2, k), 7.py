
def minimum_time(n, l, v1, v2, k):
    time_taken = l / v1  # All pupils walking
    buses_needed = (n + k - 1) // k  # Calculate number of buses needed
    time_taken += (l - l / (v2 * buses_needed)) / v2  # Account for buses
    return time_taken

# Input parsing
n, l, v1, v2, k = map(int, input().split())

# Call function and print the result with 10 decimal places
print("{:.10f}".format(minimum_time(n, l, v1, v2, k)))
```
