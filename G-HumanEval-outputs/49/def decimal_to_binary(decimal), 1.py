ON]
def decimal_to_binary(decimal):
    binary_str = bin(decimal)[2:]
    return 'db' + binary_str + 'db'

print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db100000db"
