
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    target = a[n // 2]
    
    count = 0
    for i in range(n // 2, n):
        if a[i] < target:
            count += target - a[i]
        if count > k:
            return count

    return count

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(min_moves_to_equal_elements(n, k, a))
