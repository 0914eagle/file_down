
def count_progression_terms(b_1, q, l, m, bad_integers):
    terms = set()
    current_term = b_1
    while abs(current_term) <= l:
        if current_term not in bad_integers:
            terms.add(current_term)
        if q == 1:
            break
        current_term *= q
    return len(terms) if len(terms) < float('inf') else 'inf'

# Input processing
b_1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

# Calculate and print the number of progression terms
result = count_progression_terms(b_1, q, l, m, bad_integers)
print(result)
```
