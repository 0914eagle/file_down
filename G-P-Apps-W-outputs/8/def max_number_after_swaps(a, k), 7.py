
def max_number_after_swaps(a, k):
    a_str = str(a)
    a_list = list(a_str)
    n = len(a_list)
    for i in range(n):
        max_digit = a_list[i]
        max_idx = i
        for j in range(i+1, min(i+k+1, n)):
            if a_list[j] > max_digit:
                max_digit = a_list[j]
                max_idx = j
        for j in range(max_idx, i, -1):
            a_list[j], a_list[j-1] = a_list[j-1], a_list[j]
            k -= 1
            if k == 0:
                break
        if k == 0:
            break
    return int("".join(a_list))

# Input
a, k = map(int, input().split())
# Output
print(max_number_after_swaps(a, k))
```
