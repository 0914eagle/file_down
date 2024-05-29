
def octal_to_hexadecimal(octal_num):
    decimal_num = int(octal_num, 8)
    hex_num = hex(decimal_num)[2:].upper()
    return hex_num

# Reading input
octal_num = input().strip()

# Converting octal number to hexadecimal
hexadecimal_num = octal_to_hexadecimal(octal_num)
print(hexadecimal_num)
```
