
def find_best_trip_day(n, temperatures):
    min_max_temp = float('inf')
    best_start_day = 1
    
    for i in range(n - 2):
        max_temp = max(temperatures[i], temperatures[i + 2])
        if max_temp < min_max_temp:
            min_max_temp = max_temp
            best_start_day = i + 2
    
    return best_start_day, min_max_temp

# Read input
n = int(input())
temperatures = list(map(int, input().split()))

# Find the best trip day
best_day, max_temp = find_best_trip_day(n, temperatures)

# Output the result
print(best_day, max_temp)