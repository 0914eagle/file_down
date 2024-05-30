
def restore_password(O, E):
    password = ""
    i = 0
    j = 0
    while i < len(O) or j < len(E):
        if i < len(O):
            password += O[i]
            i += 1
        if j < len(E):
            password += E[j]
            j += 1
    return password

O = input().strip()
E = input().strip()
print(restore_password(O, E))
```
