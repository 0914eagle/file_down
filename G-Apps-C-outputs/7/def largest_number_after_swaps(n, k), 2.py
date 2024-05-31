
def largest_number_after_swaps(n, k):
    n_str = str(n)
    n_list = list(n_str)
    for i in range(len(n_list)):
        max_digit = max(n_list[i:])
        if n_list[i] != max_digit:
            max_index = n_list.index(max_digit)
            n_list[i], n_list[max_index] = n_list[max_index], n_list[i]
            k -= 1
            if k == 0:
                break
    return int(''.join(n_list))

# Input
n, k = map(int, input().split())

# Output
print(largest_number_after_swaps(n, k))
