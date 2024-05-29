
# Read the input
num_octal = input().strip()

# Convert octal to decimal
num_decimal = int(num_octal, 8)

# Convert decimal to hexadecimal
num_hexadecimal = hex(num_decimal)[2:].upper()

print(num_hexadecimal)
```
