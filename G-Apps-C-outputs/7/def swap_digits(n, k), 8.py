
def swap_digits(n, k):
    n_str = str(n)
    n_list = list(n_str)
    
    for i in range(len(n_list)):
        if k == 0:
            break
        
        max_digit = max(n_list[i:])
        if n_list[i] != max_digit:
            max_digit_index = n_list[i:].index(max_digit) + i
            if i != max_digit_index:
                n_list[i], n_list[max_digit_index] = n_list[max_digit_index], n_list[i]
                k -= 1
                
    return int("".join(n_list))

# Input
n, k = map(int, input().split())

# Output
print(swap_digits(n, k))
