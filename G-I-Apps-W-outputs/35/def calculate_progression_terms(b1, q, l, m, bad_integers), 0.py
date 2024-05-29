
def calculate_progression_terms(b1, q, l, m, bad_integers):
    if q == 0:
        if b1 in bad_integers or abs(b1) > l:
            return 0
        else:
            return "inf"
    
    if q == 1 or q == -1:
        if b1 in bad_integers or abs(b1) > l:
            return 0
        else:
            return "inf"
    
    if q > 1 or q < -1:
        if b1 in bad_integers:
            return 0
        
        count = 1
        while abs(b1) <= l:
            b1 *= q
            if b1 in bad_integers:
                return count
            count += 1
        
        return count - 1

# Input
b1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

# Output
result = calculate_progression_terms(b1, q, l, m, bad_integers)
print(result)
```
