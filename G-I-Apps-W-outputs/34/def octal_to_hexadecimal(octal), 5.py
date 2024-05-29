
def octal_to_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)[2:].upper()
    return hexadecimal

# Read the input
octal_number = input().strip()

# Convert octal to hexadecimal and print the result
print(octal_to_hexadecimal(octal_number))
```
