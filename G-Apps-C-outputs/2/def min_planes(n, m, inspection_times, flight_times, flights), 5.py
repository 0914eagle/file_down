
import heapq

def min_planes(n, m, inspection_times, flight_times, flights):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append((j, flight_times[i][j]))
    
    flights.sort(key=lambda x: x[2])
    
    planes = []
    cnt = 0
    for flight in flights:
        s, f, t = flight
        while planes and planes[0] <= t:
            heapq.heappop(planes)
        if len(planes) == 0:
            cnt += 1
        heapq.heappush(planes, t + inspection_times[s-1] + flight_times[s-1][f-1])
    
    return cnt

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Call the function
result = min_planes(n, m, inspection_times, flight_times, flights)
print(result)
