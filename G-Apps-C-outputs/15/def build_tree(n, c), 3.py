
def build_tree(n, c):
    total_nodes = sum(c)
    if total_nodes != n:
        return "NO"
    
    for i in range(n):
        if c[i] == 1:
            if i != 0 and all(child == 1 for child in c[:i]):
                return "NO"
    
    return "YES"

# Input parsing
n = int(input())
c = list(map(int, input().split()))

# Call the function and print the result
print(build_tree(n, c))
