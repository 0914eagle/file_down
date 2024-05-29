
def construct_tree(n, d, k):
    if n == 1:
        print("YES")
        print("1")
        return
    
    if d >= n:
        print("NO")
        return
    
    if k < 2:
        print("NO")
        return
    
    if d == 1 and n > 2:
        print("NO")
        return
    
    if d * 2 > n:
        print("NO")
        return
    
    edges = []
    for i in range(1, d + 1):
        edges.append((i, i + 1))
    
    curr_vertex = d + 2
    for i in range(d + 1, n):
        edges.append((i, curr_vertex))
        curr_vertex += 1
    
    print("YES")
    for edge in edges:
        print(edge[0], edge[1])

# Read input
n, d, k = map(int, input().split())
# Call the function
construct_tree(n, d, k)
```
