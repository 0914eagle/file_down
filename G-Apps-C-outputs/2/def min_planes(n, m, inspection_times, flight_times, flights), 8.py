
def min_planes(n, m, inspection_times, flight_times, flights):
    def floyd_warshall(graph):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        return graph

    def find_path_cost(start, end, time):
        return inspection_times[start-1] + flight_times[start-1][end-1] + time

    flight_times = floyd_warshall(flight_times)
    max_time = max([flight[2] for flight in flights])

    dp = [[float('inf')] * (n + 1) for _ in range(max_time + 1)]
    dp[0][flights[0][0]] = 0

    for t in range(1, max_time + 1):
        for i in range(1, n + 1):
            dp[t][i] = min(dp[t - 1][j] + find_path_cost(j, i, t) for j in range(1, n + 1))

    min_planes = float('inf')
    for t in range(max_time + 1):
        for i in range(1, n + 1):
            min_planes = min(min_planes, (dp[t][i] + inspection_times[i-1] + flight_times[i-1][flights[-1][1]-1]) // max_time + 1)

    return min_planes

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the result
print(min_planes(n, m, inspection_times, flight_times, flights))
