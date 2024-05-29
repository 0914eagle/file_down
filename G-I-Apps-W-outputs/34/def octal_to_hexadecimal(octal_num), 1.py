
def octal_to_hexadecimal(octal_num):
    decimal_num = int(octal_num, 8)
    hexadecimal_num = hex(decimal_num).lstrip("0x").upper()
    return hexadecimal_num

octal_input = input().strip()
print(octal_to_hexadecimal(octal_input))
```
