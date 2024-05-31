
def can_build_rooted_tree(n, c):
    total_nodes = sum(c)
    if total_nodes != n:
        return "NO"

    for num in c:
        if num == 1:
            return "NO"

    return "YES"

# Read input
n = int(input())
c = list(map(int, input().split()))

# Call the function and print the output
print(can_build_rooted_tree(n, c))
