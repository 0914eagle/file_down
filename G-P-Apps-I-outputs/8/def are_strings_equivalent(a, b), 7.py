
def are_strings_equivalent(a, b):
    if a == b:
        return True
    if sorted(a[:len(a)//2]) == sorted(b[:len(b)//2]) and sorted(a[len(a)//2:]) == sorted(b[len(b)//2:]):
        return True
    if sorted(a[:len(a)//2]) == sorted(b[len(b)//2:]) and sorted(a[len(a)//2:]) == sorted(b[:len(b)//2]):
        return True
    return False

a = input().strip()
b = input().strip()

if are_strings_equivalent(a, b):
    print("YES")
else:
    print("NO")
```
