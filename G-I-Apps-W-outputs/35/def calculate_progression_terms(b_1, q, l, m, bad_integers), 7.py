
def calculate_progression_terms(b_1, q, l, m, bad_integers):
    if q == 0:
        if b_1 in bad_integers:
            return 0
        if abs(b_1) <= l:
            return 1
        else:
            return 0

    if q == 1:
        if b_1 in bad_integers or abs(b_1) > l:
            return 0
        else:
            return "inf"

    if q == -1:
        if b_1 in bad_integers:
            return 0
        if abs(b_1) <= l or b_1 == -l:
            return "inf"
        else:
            return 0

    terms_count = 0
    while abs(b_1) <= l:
        terms_count += 1
        if b_1 in bad_integers:
            return terms_count
        b_1 *= q

    return terms_count

# Reading input
b_1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

# Calculating and printing the result
result = calculate_progression_terms(b_1, q, l, m, bad_integers)
print(result)
```
