
def count_magical_colours(N, Q, colours, parents, queries):
    tree = {}
    for i in range(N):
        tree[i+1] = {'colour': colours[i], 'children': []}
    for i in range(N-1):
        parent = parents[i]
        tree[parent]['children'].append(i+2)

    def dfs(node):
        nonlocal tree
        count = {}
        for child in tree[node]['children']:
            child_count = dfs(child)
            for col, col_count in child_count.items():
                if col not in count:
                    count[col] = 0
                count[col] += col_count
        if tree[node]['colour'] not in count:
            count[tree[node]['colour']] = 0
        count[tree[node]['colour']] += 1
        magical_count = 0
        for col, col_count in count.items():
            if col_count % 2 != 0:
                magical_count += 1
        return count

    result = []
    for query in queries:
        K, X = query
        if K == 0:
            result.append(dfs(X))
        else:
            tree[X]['colour'] = K

    return result

# Input
N, Q = map(int, input().split())
colours = list(map(int, input().split()))
parents = list(map(int, input().split()))
queries = []
for _ in range(Q):
    K, X = map(int, input().split())
    queries.append((K, X))

# Output
results = count_magical_colours(N, Q, colours, parents, queries)
for res in results:
    print(sum(1 for val in res.values() if val % 2 != 0))
```
