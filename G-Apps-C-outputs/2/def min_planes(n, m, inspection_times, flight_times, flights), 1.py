
import heapq

def min_planes(n, m, inspection_times, flight_times, flights):
    def dijkstra(start, end):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight in enumerate(flight_times[node]):
                if weight == -1:
                    continue
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return dist[end]
    
    planes_needed = 0
    for flight in flights:
        start, end, time = flight
        inspection_time = inspection_times[start-1]
        flight_time = dijkstra(start-1, end-1)
        
        if time < inspection_time + flight_time:
            planes_needed += 1
    
    return planes_needed

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [tuple(map(int, input().split())) for _ in range(m)]

# Output minimum number of planes needed
print(min_planes(n, m, inspection_times, flight_times, flights))
