
def convert_octal_to_hex(octal_num):
    decimal_num = int(octal_num, 8)
    hex_num = hex(decimal_num)[2:]
    return hex_num.upper()

# Read input
octal_input = input().strip()

# Call the function and output result
print(convert_octal_to_hex(octal_input))
```
