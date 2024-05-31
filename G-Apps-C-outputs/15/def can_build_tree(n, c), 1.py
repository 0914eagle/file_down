
def can_build_tree(n, c):
    total_nodes = sum(c)
    if total_nodes != n:
        return "NO"
    
    for i in range(n):
        if c[i] == 1:
            if n - 1 - i < 2:
                return "NO"
    
    return "YES"

# Input reading
n = int(input())
c = list(map(int, input().split()))

# Call the function and print the result
print(can_build_tree(n, c))
