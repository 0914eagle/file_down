
import heapq

def min_planes(n, m, inspection_times, flight_times, flights):
    graph = flight_times
    planes = 0
    flights_sorted = sorted(flights, key=lambda x: x[2])
    
    for flight in flights_sorted:
        start, end, time = flight
        available_planes = []
        
        for i in range(start):
            heapq.heappush(available_planes, inspection_times[i])
        
        current_time = time
        while available_planes:
            if available_planes[0] <= current_time:
                heapq.heappop(available_planes)
            else:
                planes += 1
                break
        
        heapq.heappush(available_planes, current_time + graph[start-1][end-1])
    
    return planes + len(available_planes)

# Input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Output
print(min_planes(n, m, inspection_times, flight_times, flights))
