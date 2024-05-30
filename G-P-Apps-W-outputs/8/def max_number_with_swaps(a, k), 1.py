
def max_number_with_swaps(a, k):
    a_str = list(str(a))
    n = len(a_str)
    swapped = 0
    
    for i in range(n):
        max_digit = a_str[i]
        max_idx = i
        
        for j in range(i+1, min(n, i+k+1)):
            if a_str[j] > max_digit:
                max_digit = a_str[j]
                max_idx = j
        
        for j in range(max_idx, i, -1):
            a_str[j], a_str[j-1] = a_str[j-1], a_str[j]
            swapped += 1
            if swapped == k:
                break
        
        if swapped == k:
            break
    
    return int("".join(a_str))

# Input parsing
a, k = map(int, input().split())

# Output
print(max_number_with_swaps(a, k))
```
