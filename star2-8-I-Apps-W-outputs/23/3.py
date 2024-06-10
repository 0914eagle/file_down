
from sys import stdin, stdout

def dfs(tree, visited, graph):
    visited.add(tree)
    
    for neighbour in graph[tree]:
        if neighbour not in visited:
            dfs(neighbour, visited, graph)

def beehive_colony(trees, paths):
    graph = [set() for _ in range(trees)]
    
    for path in paths:
        graph[path[0]].add(path[1])
        graph[path[1]].add(path[0])
    
    visited = set()
    
    dfs(0, visited, graph)
    
    if len(visited) == trees:
        return trees
    else:
        return 'impossible'
    
trees, paths = map(int, stdin.readline().split())

paths_list = []

for _ in range(paths):
    paths_list.append(list(map(int, stdin.readline().split())))
    
stdout.write(str(beehive_colony(trees, paths_list)))

