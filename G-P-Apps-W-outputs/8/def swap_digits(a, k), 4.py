
def swap_digits(a, k):
    a = list(str(a))
    n = len(a)
    for i in range(n):
        if k == 0:
            break
        max_digit = max(a[i:])
        if a[i] != max_digit:
            max_index = a.index(max_digit, i)
            a[i], a[max_index] = a[max_index], a[i]
            k -= 1
    return int(''.join(a))

# Input
a, k = map(int, input().split())
# Output
print(swap_digits(a, k))
```
