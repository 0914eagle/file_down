
def min_planes(n, m, inspection_times, flight_times, flights):
    def floyd_warshall(dist, n):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    dist = flight_times.copy()

    floyd_warshall(dist, n)

    planes_needed = 0
    for flight in flights:
        start, end, time = flight
        time_to_arrive = time + dist[start-1][end-1]
        if time_to_arrive > inspection_times[end-1]:
            planes_needed += 1

    return planes_needed

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Calculate and output result
result = min_planes(n, m, inspection_times, flight_times, flights)
print(result)
