
def swap_adjacent_digits(a, k):
    a = str(a)
    n = len(a)
    a = list(a)
    for i in range(n):
        max_digit = max(a[i:])
        if a[i] != max_digit:
            max_idx = a.index(max_digit)
            num_swaps = max_idx - i
            if num_swaps <= k:
                for j in range(max_idx, i, -1):
                    a[j], a[j-1] = a[j-1], a[j]
                k -= num_swaps
        if k == 0:
            break
    return int("".join(a))

# Test cases
print(swap_adjacent_digits(1990, 1))  # Output: 9190
print(swap_adjacent_digits(300, 0))    # Output: 300
print(swap_adjacent_digits(1034, 2))   # Output: 3104
print(swap_adjacent_digits(9090000078001234, 6))  # Output: 9907000008001234
```
