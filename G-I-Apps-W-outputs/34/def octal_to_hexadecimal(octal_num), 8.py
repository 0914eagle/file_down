
def octal_to_hexadecimal(octal_num):
    decimal_num = int(octal_num, 8)
    hexadecimal_num = hex(decimal_num)[2:].upper()
    return hexadecimal_num

# Reading input
octal_num = input().strip()

# Converting octal to hexadecimal and printing output
print(octal_to_hexadecimal(octal_num))
```
