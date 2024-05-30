
def check_equivalent_strings(a, b):
    if a == b:
        return "YES"
    
    half_length = len(a) // 2
    a1 = a[:half_length]
    a2 = a[half_length:]
    b1 = b[:half_length]
    b2 = b[half_length:]
    
    if (a1 == b1 and a2 == b2) or (a1 == b2 and a2 == b1):
        return "YES"
    else:
        return "NO"

# Input
a = input().strip()
b = input().strip()

# Output
print(check_equivalent_strings(a, b))
```
