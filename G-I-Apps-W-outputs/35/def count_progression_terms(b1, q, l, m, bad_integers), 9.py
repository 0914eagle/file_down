
def count_progression_terms(b1, q, l, m, bad_integers):
    if q == 0:
        if b1 in bad_integers:
            return 0
        else:
            return 1 if abs(b1) <= l else 0
    elif q == 1:
        if b1 in bad_integers:
            return 0
        else:
            return "inf" if abs(b1) <= l else 0
    else:
        terms = set()
        current_term = b1
        while abs(current_term) <= l:
            if current_term not in bad_integers:
                terms.add(current_term)
            current_term *= q
            if current_term in terms or current_term in bad_integers:
                break
        return len(terms)

# Input parsing
b1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

# Calculate and print the result
result = count_progression_terms(b1, q, l, m, bad_integers)
print(result)
```
