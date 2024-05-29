
def construct_tree(n, d, k):
    if d >= n:
        print("NO")
        return
    
    if k < 2:
        print("NO")
        return

    tree = []
    for i in range(2, min(n, d + 2)):
        tree.append((i, i - 1))
    
    if n > d + 1:
        tree.append((1, d + 2))
        for i in range(d + 3, n + 1):
            for j in range(2, min(i - 1, k - 1) + 1):
                tree.append((i, i - j))
    
    print("YES")
    for edge in tree:
        print(edge[0], edge[1])

# Input parsing
n, d, k = map(int, input().split())

# Call the function
construct_tree(n, d, k)
```
