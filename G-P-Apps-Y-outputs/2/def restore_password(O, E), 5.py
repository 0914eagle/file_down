
def restore_password(O, E):
    password = []
    for char_odd, char_even in zip(O, E):
        password.append(char_odd)
        password.append(char_even)
    if len(O) > len(E):
        password.append(O[-1])
    return ''.join(password)

# Input
O = input().strip()
E = input().strip()

# Output
print(restore_password(O, E))
```
