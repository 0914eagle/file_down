
def count_progression_terms(b_1, q, l, m, bad_integers):
    if b_1 == 0:
        if 0 in bad_integers:
            return 0
        else:
            return "inf"
    elif q == 0:
        if b_1 in bad_integers:
            return 0
        else:
            return "inf"
    
    terms_count = 1
    current_term = b_1

    while abs(current_term) <= l:
        if current_term in bad_integers:
            return 0
        
        current_term *= q
        terms_count += 1
    
    return terms_count - 1

# Input parsing
b_1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

result = count_progression_terms(b_1, q, l, m, bad_integers)
print(result)
```
