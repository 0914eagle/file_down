
def isConnected(graph, start, end):
    if start == end:
        return True
    
    visited = [False] * len(graph)
    
    stack = [start]
    
    while len(stack) > 0:
        current = stack.pop()
        
        if current == end:
            return True
        
        if visited[current]:
            continue
        
        visited[current] = True
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                stack.append(neighbor)
    
    return False


def buildRoads(gangs):
    graph = {}
    
    for i in range(len(gangs)):
        graph[i] = []
    
    for i in range(1, len(gangs)):
        graph[i-1].append(i)
        graph[i].append(i-1)
    
    for i in range(len(gangs)-1):
        if gangs[i] == gangs[i+1]:
            return "NO"
    
    for i in range(len(gangs)):
        for j in range(i+1, len(gangs)):
            if gangs[i] != gangs[j] and isConnected(graph, i, j):
                return "NO"
    
    result = "YES\n"
    
    for i in range(1, len(gangs)):
        result += str(i) + " " + str(i+1) + "\n"
    
    return result


t = int(input())

for _ in range(t):
    n = int(input())
    
    gangs = list(map(int, input().split()))
    
    print(buildRoads(gangs))

