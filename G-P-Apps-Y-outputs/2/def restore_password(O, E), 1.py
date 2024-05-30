
def restore_password(O, E):
    original_password = ''
    i, j = 0, 0

    while i < len(O) or j < len(E):
        if i < len(O):
            original_password += O[i]
            i += 1
        if j < len(E):
            original_password += E[j]
            j += 1

    return original_password

# Input
O = input().strip()
E = input().strip()

# Output
print(restore_password(O, E))
```
