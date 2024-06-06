
from collections import defaultdict

def dijkstra(graph, start, end):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = destinations[next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Impossible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def main():
    n, r = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(r):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    f = int(input())
    for _ in range(f):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    path = dijkstra(graph, 1, 1)
    print(path)

if __name__ == '__main__':
    main()
