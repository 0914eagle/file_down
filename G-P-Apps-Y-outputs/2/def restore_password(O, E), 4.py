
def restore_password(O, E):
    password = ''
    for i in range(min(len(O), len(E))):
        password += O[i] + E[i]
    if len(O) > len(E):
        password += O[-1]
    return password

# Input
O = input()
E = input()

# Output
print(restore_password(O, E))
```
