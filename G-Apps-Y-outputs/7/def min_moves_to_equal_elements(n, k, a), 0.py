
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    median = a[n//2]
    
    # Count the number of elements less than or equal to the median
    less_than_median = sum(1 for x in a if x <= median)
    
    # If there are at least k elements less than or equal to the median, we can make them all equal to the median
    if less_than_median >= k:
        return sum(median - x for x in a[:less_than_median - k])
    else:
        # If there are less than k elements less than or equal to the median, we need to make the remaining elements equal to the median
        return sum(x - median for x in a[less_than_median:n - (k - less_than_median)])

# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(min_moves_to_equal_elements(n, k, a))
