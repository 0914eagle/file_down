
def construct_tree(n, d, k):
    if d >= n:
        print("NO")
        return
    
    if k == 1:
        if n == 1:
            print("YES")
            return
        else:
            print("NO")
            return
    
    if d == 1:
        if n > k + 1:
            print("NO")
            return
        
        print("YES")
        for i in range(2, n+1):
            print("1", i)
    
    if d > 2 * k:
        print("NO")
        return
    
    tree = []
    for i in range(2, d+2):
        tree.append((1, i))
    
    curr_node = 2
    prev_end = d + 1
    while curr_node < n:
        for i in range(2, k+1):
            if curr_node >= n:
                break
            tree.append((prev_end, curr_node+1))
            curr_node += 1
        prev_end += 1
    
    if len(tree) == n - 1:
        print("YES")
        for edge in tree:
            print(edge[0], edge[1])
    else:
        print("NO")

# Read input
n, d, k = map(int, input().split())

# Call the function
construct_tree(n, d, k)
```
