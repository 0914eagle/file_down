
def max_number_with_swaps(a, k):
    a = list(str(a))
    n = len(a)
    for i in range(n):
        max_digit = a[i]
        max_index = i
        for j in range(i+1, min(i+k+1, n)):
            if a[j] > max_digit:
                max_digit = a[j]
                max_index = j
        for j in range(max_index, i, -1):
            a[j], a[j-1] = a[j-1], a[j]
            k -= 1
            if k == 0:
                break
        if k == 0:
            break
    return int(''.join(a))

# Input
a, k = map(int, input().split())
# Output
print(max_number_with_swaps(a, k))
```
