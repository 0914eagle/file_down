
def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return 'db' + binary_str + 'db'

# Test cases
print(decimal_to_binary(15))  # Output: "db1111db"
print(decimal_to_binary(32))  # Output: "db100000db"
```
