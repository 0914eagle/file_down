
def are_equivalent_strings(a, b):
    if a == b:
        return True

    mid = len(a) // 2
    a1 = a[:mid]
    a2 = a[mid:]
    b1 = b[:mid]
    b2 = b[mid:]

    if (are_equivalent_strings(a1, b1) and are_equivalent_strings(a2, b2)) or \
       (are_equivalent_strings(a1, b2) and are_equivalent_strings(a2, b1)):
        return True

    return False

# Input
a = input().strip()
b = input().strip()

# Output
if are_equivalent_strings(a, b):
    print("YES")
else:
    print("NO")
```
