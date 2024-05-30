
def restore_password(O, E):
    original_password = ""
    for i in range(max(len(O), len(E))):
        if i < len(O):
            original_password += O[i]
        if i < len(E):
            original_password += E[i]
    return original_password

O = input().strip()
E = input().strip()
print(restore_password(O, E))
```
