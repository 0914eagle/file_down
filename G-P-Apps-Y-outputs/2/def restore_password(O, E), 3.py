
def restore_password(O, E):
    password = ''
    i, j = 0, 0
    while i < len(O) or j < len(E):
        if i < len(O):
            password += O[i]
            i += 1
        if j < len(E):
            password += E[j]
            j += 1
    return password

# Reading input from Standard Input
O = input().strip()
E = input().strip()

# Restoring the original password and printing it
print(restore_password(O, E))
```
