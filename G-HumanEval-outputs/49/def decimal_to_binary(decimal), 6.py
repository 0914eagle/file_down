
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convert decimal to binary and remove '0b' prefix
    return 'db' + binary + 'db'

# Test cases
print(decimal_to_binary(15))  # returns "db1111db"
print(decimal_to_binary(32))  # returns "db100000db"
```
