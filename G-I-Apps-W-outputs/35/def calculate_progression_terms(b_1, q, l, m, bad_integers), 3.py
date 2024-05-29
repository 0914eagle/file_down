
def calculate_progression_terms(b_1, q, l, m, bad_integers):
    terms_count = 0
    current_term = b_1
    
    if b_1 in bad_integers:
        return 0
    
    while abs(current_term) <= l:
        if current_term in bad_integers:
            return terms_count
        
        terms_count += 1
        current_term *= q
        
        if q == 0:
            break
            
    return "inf"

# Input parsing
b_1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

# Calculate and print the result
result = calculate_progression_terms(b_1, q, l, m, bad_integers)
print(result)
```
