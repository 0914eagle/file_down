
def min_time_to_deliver_all_candies(n, m, candies):
    stations_time = [0] * n
    
    for i in range(n):
        time = 0
        for j in range(m):
            start_station = i + 1
            dest_station = candies[j][1]
            if dest_station < start_station:
                time = max(time, dest_station + n - start_station)
            else:
                time = max(time, dest_station - start_station)
        
        for j in range(m):
            start_station = i + 1
            dest_station = candies[j][0]
            if dest_station < start_station:
                time = max(time, dest_station + n - start_station)
            else:
                time = max(time, dest_station - start_station)
        
        stations_time[i] = time + m

    return stations_time

# Parse input
n, m = map(int, input().split())
candies = []
for _ in range(m):
    candies.append(list(map(int, input().split())))

# Calculate and print output
output = min_time_to_deliver_all_candies(n, m, candies)
print(*output)
