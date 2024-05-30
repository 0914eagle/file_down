
from collections import defaultdict

def check_path(n, edges, queries):
    adj_list = defaultdict(list)
    
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def dfs(u, parent, query_set):
        for v in adj_list[u]:
            if v != parent:
                new_query_set = query_set.copy()
                new_query_set.add(v)
                new_query_set |= {x for x in query_set if x in adj_list[v]}
                if not new_query_set.isdisjoint(query_set):
                    return True
                if dfs(v, u, new_query_set):
                    return True
        return False
    
    for query in queries:
        query_set = set(query[1:])
        if 1 in query_set or dfs(1, -1, query_set):
            print("YES")
        else:
            print("NO")

# Input parsing
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [list(map(int, input().split()))[1:] for _ in range(m)]

# Function call
check_path(n, edges, queries)
