
def can_build_tree(n, c):
    total_nodes = sum(c)
    if total_nodes != 2*n - 1:
        return "NO"
    
    for i in range(n):
        if c[i] == 1 and i != n-1:
            return "NO"
    
    return "YES"

# Input parsing
n = int(input())
c = list(map(int, input().split()))

# Check if a tree can be built
result = can_build_tree(n, c)
print(result)
