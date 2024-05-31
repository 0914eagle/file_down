
def largest_after_swaps(n, k):
    n_str = str(n)
    n_list = list(n_str)
    sorted_indices = sorted(range(len(n_list)), key=lambda x: -int(n_list[x]))

    swaps = 0
    i = 0
    while swaps < k and i < len(n_list):
        max_index = sorted_indices[i]
        if max_index != i:
            n_list[i], n_list[max_index] = n_list[max_index], n_list[i]
            swaps += 1
        i += 1

    return int("".join(n_list))

# Read input
n, k = map(int, input().strip().split())

# Output the result
print(largest_after_swaps(n, k))
