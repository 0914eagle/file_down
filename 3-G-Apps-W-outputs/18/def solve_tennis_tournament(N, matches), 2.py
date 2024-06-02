
def solve_tennis_tournament(N, matches):
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            graph[i].append(matches[i][j] - 1)
    
    for i in range(N):
        visited = [False] * N
        day = 0
        while not all(visited):
            day += 1
            current = i
            while not visited[current]:
                visited[current] = True
                current = graph[current][0]
        if day == N:
            return N
    return -1

# Read input
N = int(input())
matches = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
result = solve_tennis_tournament(N, matches)
print(result)
