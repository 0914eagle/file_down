
def solve_tree_configuration(n, edges):
    degrees = [0] * (n + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    
    leaf_count = 0
    for degree in degrees:
        if degree == 1:
            leaf_count += 1
    
    if leaf_count == 2 or n == 2:
        return "YES"
    else:
        return "NO"

# Read input
n = int(input())
edges = [list(map(int, input().split())) for _ in range(n - 1)]

# Call the function and print the result
print(solve_tree_configuration(n, edges))
