
def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]  # Convert decimal to binary string, remove '0b' at the beginning
    return 'db' + binary_str + 'db'

# Test cases
print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db100000db"
```
