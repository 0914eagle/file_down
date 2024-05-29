
def convert_octal_to_hex(octal_num):
    decimal_num = int(octal_num, 8)
    hex_num = hex(decimal_num)[2:].upper()
    return hex_num

# Read input from user
octal_num = input()
result = convert_octal_to_hex(octal_num)
print(result)
```
