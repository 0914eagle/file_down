
def decimal_to_binary(decimal):
    binary_num = bin(decimal)[2:]  # Convert decimal to binary string
    return f"db{binary_num}db"

# Test cases
print(decimal_to_binary(15))   # "db1111db"
print(decimal_to_binary(32))   # "db100000db"
```
