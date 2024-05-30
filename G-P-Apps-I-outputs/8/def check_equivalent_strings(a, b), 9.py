
def check_equivalent_strings(a, b):
    if a == b:
        return "YES"

    n = len(a)
    if n % 2 == 1 or sorted(a) != sorted(b):
        return "NO"

    a1, a2 = a[:n//2], a[n//2:]
    b1, b2 = b[:n//2], b[n//2:]

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
