
def build_tree(n, c):
    total_nodes = sum(c)
    max_possible_nodes = n * (n + 1) // 2
    
    if total_nodes != max_possible_nodes:
        return "NO"
    
    return "YES"

# Input parsing
n = int(input())
c = list(map(int, input().split()))

# Call the function and print the result
print(build_tree(n, c))
