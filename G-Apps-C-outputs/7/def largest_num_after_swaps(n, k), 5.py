
def largest_num_after_swaps(n, k):
    n_str = str(n)
    n_list = list(n_str)
    
    for i in range(len(n_list)):
        if k == 0:
            break
        
        max_digit = max(n_list[i:])
        if n_list[i] < max_digit:
            max_idx = n_list.index(max_digit)
            n_list[i], n_list[max_idx] = n_list[max_idx], n_list[i]
            k -= 1
    
    return int("".join(n_list))

# Read input
n, k = map(int, input().split())

# Call the function and print the result
print(largest_num_after_swaps(n, k))
