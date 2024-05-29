
def is_consistent(N, M, matches):
    graph = {i: [] for i in range(N)}
    
    for match in matches:
        player1, result, player2 = match
        if result == '=':
            if player2 not in graph[player1] and player1 not in graph[player2]:
                graph[player1].append(player2)
                graph[player2].append(player1)
            else:
                return "inconsistent"
        elif result == '>':
            if player2 in graph[player1]:
                return "inconsistent"
            graph[player1].append(player2)

    return "consistent"

# Input reading
N, M = map(int, input().split())
matches = []
for _ in range(M):
    K, result, L = input().split()
    matches.append((int(K), result, int(L)))

output = is_consistent(N, M, matches)
print(output)
```
