
def find_command_order(n, q, superiors, queries):
    # Build an adjacency list representing the tree structure of the army
    adj_list = [[] for _ in range(n)]
    for i in range(1, n):
        adj_list[superiors[i-2]].append(i)

    def dfs(officer, order):
        order.append(officer)
        for subordinate in adj_list[officer]:
            dfs(subordinate, order)

    results = []
    for query in queries:
        officer, k = query
        order = []
        dfs(officer, order)
        
        if k <= len(order):
            results.append(order[k-1])
        else:
            results.append(-1)

    return results

# Input parsing
n, q = map(int, input().split())
superiors = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Solve the problem
results = find_command_order(n, q, superiors, queries)

# Output the results
for result in results:
    print(result)
