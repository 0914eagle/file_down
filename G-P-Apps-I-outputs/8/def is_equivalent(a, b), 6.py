
def is_equivalent(a, b):
    if a == b:
        return "YES"
    
    mid = len(a) // 2
    
    a1 = a[:mid]
    a2 = a[mid:]
    b1 = b[:mid]
    b2 = b[mid:]
    
    if (is_equivalent(a1, b1) == "YES" and is_equivalent(a2, b2) == "YES") or (is_equivalent(a1, b2) == "YES" and is_equivalent(a2, b1) == "YES"):
        return "YES"
    else:
        return "NO"

# Read input strings
a = input().strip()
b = input().strip()

result = is_equivalent(a, b)
print(result)
```
