
def swap_digits(num, k):
    num_str = str(num)
    num_list = list(num_str)
    n = len(num_list)
    
    for i in range(n):
        max_digit = max(num_list[i:])
        if num_list[i] < max_digit:
            max_index = num_list[i:].index(max_digit) + i
            num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
            k -= max_index - i
        if k == 0:
            break
        
    return int(''.join(num_list))

# Read input
a, k = map(int, input().split())

# Output the result
print(swap_digits(a, k))
```
