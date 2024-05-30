
def restore_password(O, E):
    password = ''
    len_O = len(O)
    len_E = len(E)
    
    for i in range(max(len_O, len_E)):
        if i < len_O:
            password += O[i]
        if i < len_E:
            password += E[i]
    
    return password

# Read input
O = input()
E = input()

# Call the function and print the result
print(restore_password(O, E))
```
