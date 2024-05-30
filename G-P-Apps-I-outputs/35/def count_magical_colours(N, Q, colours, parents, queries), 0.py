
def count_magical_colours(N, Q, colours, parents, queries):
    tree = {}  # Represent the tree as an adjacency list
    
    for i in range(N):
        tree[i + 1] = {'colour': colours[i], 'children': []}
    
    for i in range(N - 1):
        parent = parents[i]
        child = i + 2
        tree[parent]['children'].append(child)
    
    def count_odd_colours(node):
        count = [0] * 101  # Initialize count for each colour
        result = 0
        
        def dfs(curr, parent_colour):
            nonlocal result
            count[parent_colour] += 1
            
            for child in tree[curr]['children']:
                child_colour = tree[child]['colour']
                result += count[child_colour] % 2 == 0
                count[child_colour] += 1
                dfs(child, child_colour)
            
            result += (count[parent_colour] - count[parent_colour] % 2) % 2 == 0
        
        dfs(node, tree[node]['colour'])
        return result
    
    output = []
    
    for query in queries:
        k, x = query
        
        if k == 0:
            output.append(count_odd_colours(x))
        else:
            tree[x]['colour'] = k
    
    return output

# Read input
N, Q = map(int, input().split())
colours = list(map(int, input().split()))
parents = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(Q)]

# Call the function and print the output
output = count_magical_colours(N, Q, colours, parents, queries)
for res in output:
    print(res)
```
