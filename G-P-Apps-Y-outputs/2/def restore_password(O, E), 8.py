
def restore_password(O, E):
    password = ''
    for i in range(max(len(O), len(E))):
        if i < len(O):
            password += O[i]
        if i < len(E):
            password += E[i]
    return password

O = input()
E = input()
print(restore_password(O, E))
```
