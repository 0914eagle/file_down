
def calculate_written_terms(b1, q, l, m, bad_integers):
    if q == 0:
        if b1 not in bad_integers and abs(b1) <= l:
            return 1
        else:
            return 0
    
    if q == 1:
        if b1 in bad_integers or abs(b1) > l:
            return 0
        else:
            return "inf"
    
    if q == -1:
        count = 0
        while abs(b1) <= l and b1 not in bad_integers:
            count += 1
            b1 *= -1
        return count
    
    if q > 1:
        count = 0
        while abs(b1) <= l and b1 not in bad_integers:
            count += 1
            b1 *= q
        return count
    
    if q < -1:
        count = 0
        while abs(b1) <= l and b1 not in bad_integers:
            count += 1
            b1 *= q
        return count

# Input parsing
b1, q, l, m = map(int, input().split())
bad_integers = set(map(int, input().split()))

# Calculate and print the result
result = calculate_written_terms(b1, q, l, m, bad_integers)
if result == "inf":
    print("inf")
else:
    print(result)
```
