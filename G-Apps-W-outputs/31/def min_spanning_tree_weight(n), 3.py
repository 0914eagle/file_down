
def min_spanning_tree_weight(n):
    if n % 4 == 0:
        return 0
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n+1
    if n % 4 == 3:
        return 0

n = int(input())
print(min_spanning_tree_weight(n))
