
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary string and remove the '0b' prefix
    return 'db' + binary + 'db'

# Test cases
print(decimal_to_binary(15))  # Output: "db1111db"
print(decimal_to_binary(32))  # Output: "db100000db"
```
