
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    left, right = 0, 1
    sum_left, sum_right = 0, 0
    result = float('inf')
    
    while right < n:
        sum_left += (a[right] - a[left]) * (right - left)
        
        while sum_left > k:
            sum_left -= (a[right] - a[left])
            left += 1
        
        if right - left + 1 >= k:
            result = min(result, sum_left - (k - (right - left + 1)))
        
        right += 1

    return result

# Input processing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(min_moves_to_equal_elements(n, k, a))
