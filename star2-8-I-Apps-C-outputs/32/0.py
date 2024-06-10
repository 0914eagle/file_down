
n, r = map(int, input().split())
flight_to_review = []
for _ in range(r):
    a, b, c = map(int, input().split())
    flight_to_review.append([a, b, c])

f = int(input())
additional_flight = []
for _ in range(f):
    a, b, c = map(int, input().split())
    additional_flight.append([a, b, c])

def dfs(start, end, visited, cost, flight_list, graph):
    if start == end:
        return cost
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            cost = dfs(neighbor, end, visited, cost, flight_list, graph)
            if cost:
                return cost
    
    for flight in flight_list:
        if flight[0] == start and flight[1] not in visited:
            visited.add(flight[1])
            cost = dfs(flight[1], end, visited, cost + flight[2], flight_list, graph)
            if cost:
                return cost
    
    return 0

graph = {}
for i in range(1, n + 1):
    graph[i] = []
for flight in flight_to_review + additional_flight:
    graph[flight[0]].append(flight[1])
    graph[flight[1]].append(flight[0])

min_cost = float('inf')
for flight in flight_to_review + additional_flight:
    cost = dfs(flight[0], 1, set([flight[0]]), flight[2], flight_to_review + additional_flight, graph)
    if cost:
        min_cost = min(min_cost, cost)

print(min_cost)

