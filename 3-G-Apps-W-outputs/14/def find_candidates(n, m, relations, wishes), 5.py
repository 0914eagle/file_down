
def find_candidates(n, m, relations, wishes):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    ancestors = [0] * (n + 1)
    
    for p, q in relations:
        graph[p].append(q)
        indegree[q] += 1
    
    for i in range(1, n + 1):
        ancestors[i] = i
        for j in graph[i]:
            ancestors[j] = i
    
    order = []
    for i in range(1, n + 1):
        if wishes[i] != i:
            order.append(i)
    
    for i in order:
        if indegree[i] == 0:
            return -1
    
    order.sort(key=lambda x: ancestors[x], reverse=True)
    
    return len(order), order

# Input parsing
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
wishes = [0] + list(map(int, input().split())

# Call the function and print the output
result = find_candidates(n, m, relations, wishes)
if result == -1:
    print(-1)
else:
    print(result[0])
    for man in result[1]:
        print(man)
