
def restore_password(O, E):
    password = ''
    len_O = len(O)
    len_E = len(E)
    
    if len_O == len_E:
        for i in range(len_O):
            password += O[i] + E[i]
    else:
        for i in range(len_O):
            password += O[i]
        password += E[-1]
    
    return password

# Input
O = input().strip()
E = input().strip()

# Output
print(restore_password(O, E))
```
