
def octal_to_hexadecimal(octal_num):
    decimal_num = int(octal_num, 8)
    hexadecimal_num = hex(decimal_num)[2:].upper()
    return hexadecimal_num

# Read input
octal_num = input().strip()

# Convert octal to hexadecimal
result = octal_to_hexadecimal(octal_num)
print(result)
```
