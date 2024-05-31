
def min_gold_to_finish_quest(n, m, c, friends):
    graph = [[] for _ in range(n)]
    for x, y in friends:
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    visited = [False] * n
    total_gold = 0

    for i in range(n):
        if not visited[i]:
            min_cost = float('inf')
            stack = [i]
            while stack:
                node = stack.pop()
                min_cost = min(min_cost, c[node])
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

            total_gold += min_cost

    return total_gold

# Input parsing
n, m = map(int, input().split())
c = list(map(int, input().split()))
friends = [tuple(map(int, input().split())) for _ in range(m)]

result = min_gold_to_finish_quest(n, m, c, friends)
print(result)
