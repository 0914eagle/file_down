
def restore_password(O, E):
    password = ''
    i = 0
    j = 0
    while i < len(O) and j < len(E):
        password += O[i] + E[j]
        i += 1
        j += 1
    if i < len(O):
        password += O[i]
    return password

O = input()
E = input()
print(restore_password(O, E))
```
