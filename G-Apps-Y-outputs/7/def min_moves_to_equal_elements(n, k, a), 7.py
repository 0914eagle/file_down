
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    min_val = a[0]
    max_val = a[-1]
    
    min_count = a.count(min_val)
    max_count = a.count(max_val)
    
    if min_count >= k:
        return 0
    
    if min_count + max_count < k:
        return max_val - min_val
    
    target_count = k - min_count
    num_ops = 0
    
    while target_count > 0:
        if min_count <= max_count:
            diff = a[min_count] - min_val
            inc = min(target_count, diff)
            min_val += inc
            target_count -= inc
            num_ops += inc
            min_count += 1
        else:
            diff = max_val - a[-1 - max_count]
            dec = min(target_count, diff)
            max_val -= dec
            target_count -= dec
            num_ops += dec
            max_count -= 1
    
    return num_ops

# Input processing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the result
print(min_moves_to_equal_elements(n, k, a))
