
def string_xor(a: str, b: str) -> str:
    result = ''
    for charA, charB in zip(a, b):
        if charA == charB:
            result += '0'
        else:
            result += '1'
    return result

# Test the function
print(string_xor('010', '110'))  # Output should be '100'
