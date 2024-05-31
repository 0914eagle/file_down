
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    target = a[k-1]
    moves = 0
    for i in range(k):
        moves += target - a[i]
    return moves

# Input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_moves_to_equal_elements(n, k, a))
