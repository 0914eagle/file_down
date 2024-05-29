
def calculate_progression_terms(b1, q, l, m, bad_integers):
    if q == 0:
        if b1 in bad_integers:
            return 0
        elif abs(b1) <= l:
            return 1
        else:
            return 0
    if q == 1:
        if b1 in bad_integers:
            return 0
        elif abs(b1) <= l:
            return "inf"
        else:
            return 0

    count = 0
    current_term = b1
    while abs(current_term) <= l:
        if current_term in bad_integers:
            current_term *= q
            continue
        current_term *= q
        count += 1

    return count

# Input parsing
b1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

result = calculate_progression_terms(b1, q, l, m, bad_integers)
print(result)
```
