
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    median = a[n // 2]
    
    moves = 0
    if a.count(median) >= k:
        return moves
    
    if a.count(median) + a.count(a[n // 2 - 1]) >= k:
        median = a[n // 2 - 1]
    
    for i in range(n // 2, n):
        if a[i] > median:
            moves += a[i] - median
        elif a[i] < median:
            moves += median - a[i]
        
        if k <= a.count(a[i]) + n//2:
            return moves
    
    return moves

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(min_moves_to_equal_elements(n, k, a))
