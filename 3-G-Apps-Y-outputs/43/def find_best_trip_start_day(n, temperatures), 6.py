
def find_best_trip_start_day(n, temperatures):
    min_max_temp = float('inf')
    best_start_day = 1
    
    for i in range(1, n-1):
        max_temp = max(temperatures[i-1], temperatures[i+1])
        if max_temp < min_max_temp:
            min_max_temp = max_temp
            best_start_day = i+1
    
    return best_start_day, min_max_temp

# Read input
n = int(input())
temperatures = list(map(int, input().split()))

# Find the best trip start day and maximum temperature
best_day, max_temp = find_best_trip_start_day(n, temperatures)

# Output the result
print(best_day, max_temp)
