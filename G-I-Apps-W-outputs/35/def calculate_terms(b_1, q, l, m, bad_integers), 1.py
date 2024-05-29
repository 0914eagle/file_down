
def calculate_terms(b_1, q, l, m, bad_integers):
    if b_1 in bad_integers:
        return 0
    
    if abs(b_1) > l:
        return 0
    
    if q == 1:
        if b_1 in bad_integers:
            return 0
        else:
            return "inf"

    while abs(b_1) <= l:
        if b_1 in bad_integers:
            b_1 *= q
            continue
        b_1 *= q

    return 1

# Input parsing
b_1, q, l, m = map(int, input().split())
bad_integers = list(map(int, input().split()))

# Calculate and print the result
result = calculate_terms(b_1, q, l, m, bad_integers)
print(result)
```
