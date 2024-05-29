
def octal_to_hexadecimal(num):
    decimal_num = int(num, 8)
    hexadecimal_num = hex(decimal_num)[2:].upper()
    return hexadecimal_num

# Read input
num_octal = input().strip()

# Convert and print result
print(octal_to_hexadecimal(num_octal))
```
