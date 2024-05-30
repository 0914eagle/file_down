
def max_number_after_swaps(a, k):
    a_str = str(a)
    a_list = list(a_str)
    n = len(a_list)
    
    for i in range(n):
        if k == 0:
            break
        
        max_digit = max(a_list[i:])
        max_index = a_list[i:].index(max_digit) + i
        
        if max_index != i:
            a_list[i], a_list[max_index] = a_list[max_index], a_list[i]
            k -= (max_index - i)
    
    return int("".join(a_list))

# Input
a, k = map(int, input().split())
print(max_number_after_swaps(a, k))
```
