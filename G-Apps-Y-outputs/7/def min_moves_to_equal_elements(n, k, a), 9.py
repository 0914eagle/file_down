
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    min_val = a[0]
    max_val = a[-1]
    
    min_count = a.count(min_val)
    max_count = a.count(max_val)
    
    min_moves = 0
    
    while min_count < k:
        diff = a[min_moves+1] - min_val
        if (k - min_count) * diff <= (max_count + min_moves) - k:
            min_moves += (k - min_count)
            break
        else:
            min_moves += 1
            min_val += 1
            min_count += 1

    max_moves = 0
    while max_count < k:
        diff = max_val - a[-2 - max_moves]
        if (k - max_count) * diff <= (max_moves + min_moves) - k:
            max_moves += (k - max_count)
            break
        else:
            max_moves += 1
            max_val -= 1
            max_count += 1

    return min_moves + max_moves

# Input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_moves_to_equal_elements(n, k, a))
