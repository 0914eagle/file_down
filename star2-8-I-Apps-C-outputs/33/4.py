
from collections import defaultdict


def dfs(node, visited, graph):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, visited, graph)


def find_cc(graph):
    cc = 0
    visited = set()
    for node in graph:
        if node not in visited:
            cc += 1
            dfs(node, visited, graph)
    return cc


def find_rooms(walk, graph):
    visited = set()
    for node in walk:
        visited.add(node)
    for node in graph:
        if node not in visited:
            return node
    return -1


def find_prob(graph, start, end, n):
    if n == 1:
        return 1
    prob = 0
    for neighbour in graph[start]:
        if neighbour != end:
            prob += find_prob(graph, neighbour, end, n - 1) / len(graph[start])
    return prob


def find_prob_from_rooms(graph, rooms, n):
    prob = 0
    for i in range(len(rooms) - 1):
        prob += find_prob(graph, rooms[i], rooms[i + 1], n)
    return prob


if __name__ == "__main__":
    n = int(input())
    l = int(input())
    walk = [int(x) for x in input().split()]
    graph = defaultdict(list)
    for i in range(n):
        n_i, *neighbours = [int(x) for x in input().split()]
        graph[i] = neighbours

    if n == l:
        start = find_rooms(walk, graph)
        prob = find_prob_from_rooms(graph, walk, l)
        print(prob)
    else:
        cc = find_cc(graph)
        prob = 1 / cc
        print(prob)

