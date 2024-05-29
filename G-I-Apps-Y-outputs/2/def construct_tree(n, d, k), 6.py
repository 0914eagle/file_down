
def construct_tree(n, d, k):
    if n == 1:
        print("YES")
        return
    if d >= n:
        print("NO")
        return
    if k == 1:
        if n > 2:
            print("NO")
            return
        else:
            print("YES")
            print("1 2")
            return
      
    vertices = [i+1 for i in range(1, min(d+1, n))]
    edges = []
    
    for v in vertices[1:]:
        edges.append((v, 1))
    
    curr = vertices[-1]
    for i in range(len(vertices), n):
        edges.append((curr, i+1))
        if i - d + 1 >= 1:
            edges.append((curr, i-d+1))
        curr = i + 1
    
    if len(edges) > (n-1) * k:
        print("NO")
    else:
        print("YES")
        for e in edges:
            print(e[0], e[1])

# Read input values
n, d, k = map(int, input().split())

# Call the function with the given inputs
construct_tree(n, d, k)
```
