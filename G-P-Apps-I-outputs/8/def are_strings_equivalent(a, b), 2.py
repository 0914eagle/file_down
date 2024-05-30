
def are_strings_equivalent(a, b):
    if a == b:
        return True
    
    mid = len(a) // 2
    
    a1 = a[:mid]
    a2 = a[mid:]
    
    b1 = b[:mid]
    b2 = b[mid:]
    
    if (are_strings_equivalent(a1, b1) and are_strings_equivalent(a2, b2)) or (are_strings_equivalent(a1, b2) and are_strings_equivalent(a2, b1)):
        return True
    
    return False

# Input
a = input()
b = input()

# Output
if are_strings_equivalent(a, b):
    print("YES")
else:
    print("NO")
```
